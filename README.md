# Exploring RAG with LLM's

`mkdir docs` # upload your PDF files here

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 rag.py ./docs/book1.pdf
```

## Provide the llm inputs
```
# Initialize OpenAI client
client = OpenAI(
    api_key="xxxx-xxxx-xxxx-xxxxx",
    base_url="https://chat.openai.com/api/v1"
)
```


## Sample Run
```
(venv) ➜  RAG git:(main) ✗ python3 rag.py ./docs/OWASP_Testing_Guide_v4.pdf   
INFO:__main__:Loading chunks from PDF...
INFO:__main__:Opened PDF file: ./docs/OWASP_Testing_Guide_v4.pdf
INFO:__main__:Processed page 1/224
INFO:__main__:Processed page 2/224
INFO:__main__:Processed page 3/224
INFO:__main__:Processed page 4/224
INFO:__main__:Processed page 5/224
INFO:__main__:Processed page 6/224
INFO:__main__:Processed page 7/224
INFO:__main__:Processed page 8/224
INFO:__main__:Processed page 9/224
INFO:__main__:Processed page 10/224
INFO:__main__:Processed page 11/224
INFO:__main__:Processed page 12/224
INFO:__main__:Processed page 13/224
INFO:__main__:Processed page 14/224
INFO:__main__:Processed page 15/224
INFO:__main__:Processed page 16/224
INFO:__main__:Processed page 17/224
INFO:__main__:Processed page 18/224
INFO:__main__:Processed page 19/224
INFO:__main__:Processed page 20/224
INFO:__main__:Processed page 21/224
INFO:__main__:Processed page 22/224
INFO:__main__:Processed page 23/224
INFO:__main__:Processed page 24/224
INFO:__main__:Processed page 25/224
INFO:__main__:Processed page 26/224
INFO:__main__:Processed page 27/224
INFO:__main__:Processed page 28/224
INFO:__main__:Processed page 29/224
INFO:__main__:Processed page 30/224
INFO:__main__:Processed page 31/224
INFO:__main__:Processed page 32/224
INFO:__main__:Processed page 33/224
INFO:__main__:Processed page 34/224
INFO:__main__:Processed page 35/224
INFO:__main__:Processed page 36/224
INFO:__main__:Processed page 37/224
INFO:__main__:Processed page 38/224
INFO:__main__:Processed page 39/224
INFO:__main__:Processed page 40/224
INFO:__main__:Processed page 41/224
INFO:__main__:Processed page 42/224
INFO:__main__:Processed page 43/224
INFO:__main__:Processed page 44/224
INFO:__main__:Processed page 45/224
INFO:__main__:Processed page 46/224
INFO:__main__:Processed page 47/224
INFO:__main__:Processed page 48/224
INFO:__main__:Processed page 49/224
INFO:__main__:Processed page 50/224
INFO:__main__:Processed page 51/224
INFO:__main__:Processed page 52/224
INFO:__main__:Processed page 53/224
INFO:__main__:Processed page 54/224
INFO:__main__:Processed page 55/224
INFO:__main__:Processed page 56/224
INFO:__main__:Processed page 57/224
INFO:__main__:Processed page 58/224
INFO:__main__:Processed page 59/224
INFO:__main__:Processed page 60/224
INFO:__main__:Processed page 61/224
INFO:__main__:Processed page 62/224
INFO:__main__:Processed page 63/224
INFO:__main__:Processed page 64/224
INFO:__main__:Processed page 65/224
INFO:__main__:Processed page 66/224
INFO:__main__:Processed page 67/224
INFO:__main__:Processed page 68/224
INFO:__main__:Processed page 69/224
INFO:__main__:Processed page 70/224
INFO:__main__:Processed page 71/224
INFO:__main__:Processed page 72/224
INFO:__main__:Processed page 73/224
INFO:__main__:Processed page 74/224
INFO:__main__:Processed page 75/224
INFO:__main__:Processed page 76/224
INFO:__main__:Processed page 77/224
INFO:__main__:Processed page 78/224
INFO:__main__:Processed page 79/224
INFO:__main__:Processed page 80/224
INFO:__main__:Processed page 81/224
INFO:__main__:Processed page 82/224
INFO:__main__:Processed page 83/224
INFO:__main__:Processed page 84/224
INFO:__main__:Processed page 85/224
INFO:__main__:Processed page 86/224
INFO:__main__:Processed page 87/224
INFO:__main__:Processed page 88/224
INFO:__main__:Processed page 89/224
INFO:__main__:Processed page 90/224
INFO:__main__:Processed page 91/224
INFO:__main__:Processed page 92/224
INFO:__main__:Processed page 93/224
INFO:__main__:Processed page 94/224
INFO:__main__:Processed page 95/224
INFO:__main__:Processed page 96/224
INFO:__main__:Processed page 97/224
INFO:__main__:Processed page 98/224
INFO:__main__:Processed page 99/224
INFO:__main__:Processed page 100/224
INFO:__main__:Processed page 101/224
INFO:__main__:Processed page 102/224
INFO:__main__:Processed page 103/224
INFO:__main__:Processed page 104/224
INFO:__main__:Processed page 105/224
INFO:__main__:Processed page 106/224
INFO:__main__:Processed page 107/224
INFO:__main__:Processed page 108/224
INFO:__main__:Processed page 109/224
INFO:__main__:Processed page 110/224
INFO:__main__:Processed page 111/224
INFO:__main__:Processed page 112/224
INFO:__main__:Processed page 113/224
INFO:__main__:Processed page 114/224
INFO:__main__:Processed page 115/224
INFO:__main__:Processed page 116/224
INFO:__main__:Processed page 117/224
INFO:__main__:Processed page 118/224
INFO:__main__:Processed page 119/224
INFO:__main__:Processed page 120/224
INFO:__main__:Processed page 121/224
INFO:__main__:Processed page 122/224
INFO:__main__:Processed page 123/224
INFO:__main__:Processed page 124/224
INFO:__main__:Processed page 125/224
INFO:__main__:Processed page 126/224
INFO:__main__:Processed page 127/224
INFO:__main__:Processed page 128/224
INFO:__main__:Processed page 129/224
INFO:__main__:Processed page 130/224
INFO:__main__:Processed page 131/224
INFO:__main__:Processed page 132/224
INFO:__main__:Processed page 133/224
INFO:__main__:Processed page 134/224
INFO:__main__:Processed page 135/224
INFO:__main__:Processed page 136/224
INFO:__main__:Processed page 137/224
INFO:__main__:Processed page 138/224
INFO:__main__:Processed page 139/224
INFO:__main__:Processed page 140/224
INFO:__main__:Processed page 141/224
INFO:__main__:Processed page 142/224
INFO:__main__:Processed page 143/224
INFO:__main__:Processed page 144/224
INFO:__main__:Processed page 145/224
INFO:__main__:Processed page 146/224
INFO:__main__:Processed page 147/224
INFO:__main__:Processed page 148/224
INFO:__main__:Processed page 149/224
INFO:__main__:Processed page 150/224
INFO:__main__:Processed page 151/224
INFO:__main__:Processed page 152/224
INFO:__main__:Processed page 153/224
INFO:__main__:Processed page 154/224
INFO:__main__:Processed page 155/224
INFO:__main__:Processed page 156/224
INFO:__main__:Processed page 157/224
INFO:__main__:Processed page 158/224
INFO:__main__:Processed page 159/224
INFO:__main__:Processed page 160/224
INFO:__main__:Processed page 161/224
INFO:__main__:Processed page 162/224
INFO:__main__:Processed page 163/224
INFO:__main__:Processed page 164/224
INFO:__main__:Processed page 165/224
INFO:__main__:Processed page 166/224
INFO:__main__:Processed page 167/224
INFO:__main__:Processed page 168/224
INFO:__main__:Processed page 169/224
INFO:__main__:Processed page 170/224
INFO:__main__:Processed page 171/224
INFO:__main__:Processed page 172/224
INFO:__main__:Processed page 173/224
INFO:__main__:Processed page 174/224
INFO:__main__:Processed page 175/224
INFO:__main__:Processed page 176/224
INFO:__main__:Processed page 177/224
INFO:__main__:Processed page 178/224
INFO:__main__:Processed page 179/224
INFO:__main__:Processed page 180/224
INFO:__main__:Processed page 181/224
INFO:__main__:Processed page 182/224
INFO:__main__:Processed page 183/224
INFO:__main__:Processed page 184/224
INFO:__main__:Processed page 185/224
INFO:__main__:Processed page 186/224
INFO:__main__:Processed page 187/224
INFO:__main__:Processed page 188/224
INFO:__main__:Processed page 189/224
INFO:__main__:Processed page 190/224
INFO:__main__:Processed page 191/224
INFO:__main__:Processed page 192/224
INFO:__main__:Processed page 193/224
INFO:__main__:Processed page 194/224
INFO:__main__:Processed page 195/224
INFO:__main__:Processed page 196/224
INFO:__main__:Processed page 197/224
INFO:__main__:Processed page 198/224
INFO:__main__:Processed page 199/224
INFO:__main__:Processed page 200/224
INFO:__main__:Processed page 201/224
INFO:__main__:Processed page 202/224
INFO:__main__:Processed page 203/224
INFO:__main__:Processed page 204/224
INFO:__main__:Processed page 205/224
INFO:__main__:Processed page 206/224
INFO:__main__:Processed page 207/224
INFO:__main__:Processed page 208/224
INFO:__main__:Processed page 209/224
INFO:__main__:Processed page 210/224
INFO:__main__:Processed page 211/224
INFO:__main__:Processed page 212/224
INFO:__main__:Processed page 213/224
INFO:__main__:Processed page 214/224
INFO:__main__:Processed page 215/224
INFO:__main__:Processed page 216/224
INFO:__main__:Processed page 217/224
INFO:__main__:Processed page 218/224
INFO:__main__:Processed page 219/224
INFO:__main__:Processed page 220/224
INFO:__main__:Processed page 221/224
INFO:__main__:Processed page 222/224
INFO:__main__:Processed page 223/224
INFO:__main__:Processed page 224/224
INFO:__main__:Closed PDF file.
INFO:__main__:Total text chunks loaded: 1128
INFO:__main__:Processed 8/1128 chunks
INFO:__main__:Processed 16/1128 chunks
INFO:__main__:Processed 24/1128 chunks
INFO:__main__:Processed 32/1128 chunks
INFO:__main__:Processed 40/1128 chunks
INFO:__main__:Processed 48/1128 chunks
INFO:__main__:Processed 56/1128 chunks
INFO:__main__:Processed 64/1128 chunks
INFO:__main__:Processed 72/1128 chunks
INFO:__main__:Processed 80/1128 chunks
INFO:__main__:Processed 88/1128 chunks
INFO:__main__:Processed 96/1128 chunks
INFO:__main__:Processed 104/1128 chunks
INFO:__main__:Processed 112/1128 chunks
INFO:__main__:Processed 120/1128 chunks
INFO:__main__:Processed 128/1128 chunks
INFO:__main__:Processed 136/1128 chunks
INFO:__main__:Processed 144/1128 chunks
INFO:__main__:Processed 152/1128 chunks
INFO:__main__:Processed 160/1128 chunks
INFO:__main__:Processed 168/1128 chunks
INFO:__main__:Processed 176/1128 chunks
INFO:__main__:Processed 184/1128 chunks
INFO:__main__:Processed 192/1128 chunks
INFO:__main__:Processed 200/1128 chunks
INFO:__main__:Processed 208/1128 chunks
INFO:__main__:Processed 216/1128 chunks
INFO:__main__:Processed 224/1128 chunks
INFO:__main__:Processed 232/1128 chunks
INFO:__main__:Processed 240/1128 chunks
INFO:__main__:Processed 248/1128 chunks
INFO:__main__:Processed 256/1128 chunks
INFO:__main__:Processed 264/1128 chunks
INFO:__main__:Processed 272/1128 chunks
INFO:__main__:Processed 280/1128 chunks
INFO:__main__:Processed 288/1128 chunks
INFO:__main__:Processed 296/1128 chunks
INFO:__main__:Processed 304/1128 chunks
INFO:__main__:Processed 312/1128 chunks
INFO:__main__:Processed 320/1128 chunks
INFO:__main__:Processed 328/1128 chunks
INFO:__main__:Processed 336/1128 chunks
INFO:__main__:Processed 344/1128 chunks
INFO:__main__:Processed 352/1128 chunks
INFO:__main__:Processed 360/1128 chunks
INFO:__main__:Processed 368/1128 chunks
INFO:__main__:Processed 376/1128 chunks
INFO:__main__:Processed 384/1128 chunks
INFO:__main__:Processed 392/1128 chunks
INFO:__main__:Processed 400/1128 chunks
INFO:__main__:Processed 408/1128 chunks
INFO:__main__:Processed 416/1128 chunks
INFO:__main__:Processed 424/1128 chunks
INFO:__main__:Processed 432/1128 chunks
INFO:__main__:Processed 440/1128 chunks
INFO:__main__:Processed 448/1128 chunks
INFO:__main__:Processed 456/1128 chunks
INFO:__main__:Processed 464/1128 chunks
INFO:__main__:Processed 472/1128 chunks
INFO:__main__:Processed 480/1128 chunks
INFO:__main__:Processed 488/1128 chunks
INFO:__main__:Processed 496/1128 chunks
INFO:__main__:Processed 504/1128 chunks
INFO:__main__:Processed 512/1128 chunks
INFO:__main__:Processed 520/1128 chunks
INFO:__main__:Processed 528/1128 chunks
INFO:__main__:Processed 536/1128 chunks
INFO:__main__:Processed 544/1128 chunks
INFO:__main__:Processed 552/1128 chunks
INFO:__main__:Processed 560/1128 chunks
INFO:__main__:Processed 568/1128 chunks
INFO:__main__:Processed 576/1128 chunks
INFO:__main__:Processed 584/1128 chunks
INFO:__main__:Processed 592/1128 chunks
INFO:__main__:Processed 600/1128 chunks
INFO:__main__:Processed 608/1128 chunks
INFO:__main__:Processed 616/1128 chunks
INFO:__main__:Processed 624/1128 chunks
INFO:__main__:Processed 632/1128 chunks
INFO:__main__:Processed 640/1128 chunks
INFO:__main__:Processed 648/1128 chunks
INFO:__main__:Processed 656/1128 chunks
INFO:__main__:Processed 664/1128 chunks
INFO:__main__:Processed 672/1128 chunks
INFO:__main__:Processed 680/1128 chunks
INFO:__main__:Processed 688/1128 chunks
INFO:__main__:Processed 696/1128 chunks
INFO:__main__:Processed 704/1128 chunks
INFO:__main__:Processed 712/1128 chunks
INFO:__main__:Processed 720/1128 chunks
INFO:__main__:Processed 728/1128 chunks
INFO:__main__:Processed 736/1128 chunks
INFO:__main__:Processed 744/1128 chunks
INFO:__main__:Processed 752/1128 chunks
INFO:__main__:Processed 760/1128 chunks
INFO:__main__:Processed 768/1128 chunks
INFO:__main__:Processed 776/1128 chunks
INFO:__main__:Processed 784/1128 chunks
INFO:__main__:Processed 792/1128 chunks
INFO:__main__:Processed 800/1128 chunks
INFO:__main__:Processed 808/1128 chunks
INFO:__main__:Processed 816/1128 chunks
INFO:__main__:Processed 824/1128 chunks
INFO:__main__:Processed 832/1128 chunks
INFO:__main__:Processed 840/1128 chunks
INFO:__main__:Processed 848/1128 chunks
INFO:__main__:Processed 856/1128 chunks
INFO:__main__:Processed 864/1128 chunks
INFO:__main__:Processed 872/1128 chunks
INFO:__main__:Processed 880/1128 chunks
INFO:__main__:Processed 888/1128 chunks
INFO:__main__:Processed 896/1128 chunks
INFO:__main__:Processed 904/1128 chunks
INFO:__main__:Processed 912/1128 chunks
INFO:__main__:Processed 920/1128 chunks
INFO:__main__:Processed 928/1128 chunks
INFO:__main__:Processed 936/1128 chunks
INFO:__main__:Processed 944/1128 chunks
INFO:__main__:Processed 952/1128 chunks
INFO:__main__:Processed 960/1128 chunks
INFO:__main__:Processed 968/1128 chunks
INFO:__main__:Processed 976/1128 chunks
INFO:__main__:Processed 984/1128 chunks
INFO:__main__:Processed 992/1128 chunks
INFO:__main__:Processed 1000/1128 chunks
INFO:__main__:Processed 1008/1128 chunks
INFO:__main__:Processed 1016/1128 chunks
INFO:__main__:Processed 1024/1128 chunks
INFO:__main__:Processed 1032/1128 chunks
INFO:__main__:Processed 1040/1128 chunks
INFO:__main__:Processed 1048/1128 chunks
INFO:__main__:Processed 1056/1128 chunks
INFO:__main__:Processed 1064/1128 chunks
INFO:__main__:Processed 1072/1128 chunks
INFO:__main__:Processed 1080/1128 chunks
INFO:__main__:Processed 1088/1128 chunks
INFO:__main__:Processed 1096/1128 chunks
INFO:__main__:Processed 1104/1128 chunks
INFO:__main__:Processed 1112/1128 chunks
INFO:__main__:Processed 1120/1128 chunks
INFO:__main__:Processed 1128/1128 chunks
INFO:__main__:Vector database created and embeddings added.
INFO:__main__:Vector database saved to db/OWASP_Testing_Guide_v4.faiss.


Ask a question (type 'quit' to exit): What are owasp top 10 vulns?


 Question:  What are owasp top 10 vulns?


Answer:  The OWASP Top 10 is a list of the 10 most critical web application security risks. Here are the current top 10 vulnerabilities, in no particular order:

1. Injection (SQL, OS, NoSQL)
2. Broken Authentication
3. Cross-Site Scripting (XSS)
4. Cross-Site Request Forgery (CSRF)
5. Using Components with Known Vulnerabilities
6. Security Misconfiguration
7. Sensitive Data Exposure
8. Missing Function Level Access Control
9. Insufficient Logging & Monitoring
10. Lack of Security Testing

It's important to note that these vulnerabilities are not mutually exclusive, and many web applications will have a combination of these risks. It's also worth noting that the OWASP Top 10 is updated regularly, so it's important to stay current with the latest version.


Ask a question (type 'quit' to exit): 

```