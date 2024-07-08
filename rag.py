import pymupdf
from openai import OpenAI
from transformers import BertTokenizer, BertModel
import torch
import sys
import logging
import json
import faiss
import numpy as np
import os

# Set the environment variable to allow multiple OpenMP runtimes
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a filter to exclude logs from httpx
class ExcludeHttpxFilter(logging.Filter):
    def filter(self, record):
        return not record.name.startswith('httpx')

# Add the filter to the root logger
root_logger = logging.getLogger()
root_logger.addFilter(ExcludeHttpxFilter())

# Initialize OpenAI client
client = OpenAI(
    api_key="xxxxx-xxxxx-xxxxxx",
    base_url="https://chat.openai.com/api/v1"
)

def load_chunk_pdf(pdf_file):
    # Initialize a list to store the text chunks
    text_chunks = []
    
    # Open the PDF file
    doc = pymupdf.open(pdf_file)
    logger.info(f"Opened PDF file: {pdf_file}")

    # Iterate through each page in the document
    total_pages = len(doc)
    for page_num in range(total_pages):
        page = doc.load_page(page_num)
        
        # Extract text from the page
        page_text = page.get_text()
        
        # Split the text into chunks of 1000 characters without overlap
        chunk_size = 1000
        for i in range(0, len(page_text), chunk_size):
            chunk = page_text[i:i+chunk_size]
            text_chunks.append(chunk)
        
        # Log progress for each page processed
        logger.info(f"Processed page {page_num + 1}/{total_pages}")

    # Close the document
    doc.close()
    logger.info("Closed PDF file.")
    
    return text_chunks

def embed_chunks(text_chunks):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    embeddings = []
    for i in range(0, len(text_chunks), 8):
        batch_chunks = text_chunks[i:i+8]
        inputs = tokenizer(batch_chunks, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        for j in range(len(batch_chunks)):
            embeddings.append(outputs.last_hidden_state[j, 0, :].numpy())
        logger.info(f"Processed {i + len(batch_chunks)}/{len(text_chunks)} chunks")
    return np.array(embeddings)

def create_vector_database(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    logger.info("Vector database created and embeddings added.")
    return index

def save_vector_database(index, file_path):
    faiss.write_index(index, file_path)
    logger.info(f"Vector database saved to {file_path}.")

def load_vector_database(file_path):
    index = faiss.read_index(file_path)
    logger.info(f"Vector database loaded from {file_path}.")
    return index

def search_vector_database(index, query_embedding, k=5):
    distances, indices = index.search(np.array([query_embedding]), k)
    return indices[0]

def embed_query(query, tokenizer, model):
    inputs = tokenizer([query], return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[0, 0, :].numpy()

def interact_with_llm(model, relevant_chunks, question):
  context = " ".join(relevant_chunks)
  formatted_prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
  response = client.completions.create(
      model=model,
      prompt=formatted_prompt,
      max_tokens=512,
      temperature=0,
      stream=False
  )
  return response

def main(pdf_file):
    
    # Load chunks from PDF
    logger.info("Loading chunks from PDF...")
    text_chunks = load_chunk_pdf(pdf_file)
    logger.info(f"Total text chunks loaded: {len(text_chunks)}")

    pdf_filename = os.path.basename(pdf_file)
    pdf_name, _ = os.path.splitext(pdf_filename)
    vector_db_path = os.path.join("db", f"{pdf_name}.faiss")
    
    if not os.path.exists(vector_db_path):
        embeddings = embed_chunks(text_chunks)
        index = create_vector_database(embeddings)
        os.makedirs("db", exist_ok=True)
        save_vector_database(index, vector_db_path)
    else:
        index = load_vector_database(vector_db_path)

    # Question loop
    while True:
        question = input("\n\nAsk a question (type 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased')
        query_embedding = embed_query(question, tokenizer, model)

        indices = search_vector_database(index, query_embedding)
        relevant_chunks = [text_chunks[i] for i in indices]

        model_id = "meta-llama/Llama-2-13b-chat-hf"
        print("\n\n Question: ", question)
        answer = interact_with_llm(model_id, relevant_chunks, question)
        # Assuming 'answer' contains the response as shown in your example
        for key, value in answer:
          if key == 'choices':
            for choice in value:
              answer_text = choice.text
              # Find the position of the substring "Question:"
              question_index = answer_text.find("Question:")
              # Print the text up to the "Question:" substring
              if question_index != -1:
                answer_text = answer_text[:question_index].strip()
              print("\n\nAnswer:", answer_text)
              break  # Stop after processing the first 'choices' key



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    main(pdf_file)