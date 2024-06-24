# diabetic_RAG_QA

## Introductions

## File Structure

````plaintext
.
├── diabetic_qa_vector_db
│   ├── index.faiss
│   └── index.pkl
├── diabetic_vector_db
│   ├── index.faiss
│   └── index.pkl
├── doc
│   ├── diabetic_acticles.pdf
│   └── diabetic_qa.pdf
├── with Gemini
│   ├── RAG_Gemini_sort(QA-pair).ipynb
│   ├── RAG_Gemini(article).ipynb
│   └── RAG_Gemini(QA-pair).ipynb
├── with pre-trained model
│   └── RAG_bloomz-1b7.ipynb
├── README.md
├── requirements.txt
└── create_vector_db.py
````
## Resources Used

- Python Version: 3.11.9
- IDE: VSCode
- Requirements:
  - Install [requirements](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/requirements.txt)
  ```terminal
  pip install -r requirements.txt