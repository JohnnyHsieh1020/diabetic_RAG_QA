# diabetic_RAG_QA

## Introductions
1. Utilized Retrieval Augmented Generation (RAG) to generate a simple QA system.

2. There are two kinds of external data.
   * Article about diabetic. ([Article](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/doc/diabetic_acticles.pdf))
   * QA-pair document generated from [Article](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/doc/diabetic_acticles.pdf). ([QA-pair](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/doc/diabetic_qa.pdf))

3. Generate two vector DB to store the embeddings of the corresponding external data.
    * Vector DB for article.([Article vector DB](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/tree/main/diabetic_vector_db))
    * Vector DB for qa-pair.([QA-pair vector DB](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/tree/main/diabetic_qa_vector_db))

4. Utilized two Large Language Models(LLMs) to generate the answer.
    * Pre-trained Model: bigscience/bloomz-1b7([Link](https://huggingface.co/bigscience/bloomz-1b7))
    * Gemini: gemini-pro, gemini-1.5-flash

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