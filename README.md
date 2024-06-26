# diabetic_RAG_QA

## Introductions

1. Utilized Retrieval Augmented Generation (RAG) to generate a diabetic-based simple QA system.

2. There are two kinds of external data.

   - Article about diabetic. ([Article](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/doc/diabetic_acticles.pdf))
   - QA-pair document generated from [Article](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/doc/diabetic_acticles.pdf). ([QA-pair](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/doc/diabetic_qa.pdf))

3. Generate two vector DB to store the embeddings of the corresponding external data.

   - Vector DB for article.([Article vector DB](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/tree/main/diabetic_vector_db))
   - Vector DB for qa-pair.([QA-pair vector DB](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/tree/main/diabetic_qa_vector_db))

4. Utilized two Large Language Models(LLMs) to generate the answer.

   - Pre-trained Model: bigscience/bloomz-1b7([Link](https://huggingface.co/bigscience/bloomz-1b7))
   - Gemini: gemini-pro, gemini-1.5-flash

## File Structure

```plaintext
.
├── diabetic_qa_vector_db (Vector DB for QA-pair)
│   ├── index.faiss
│   └── index.pkl
├── diabetic_vector_db (Vector DB for article)
│   ├── index.faiss
│   └── index.pkl
├── doc (external document)
│   ├── diabetic_acticles.pdf
│   └── diabetic_qa.pdf
├── with Gemini (RAG with Gemini)
│   ├── RAG_Gemini_sort(QA-pair).ipynb
│   ├── RAG_Gemini(article).ipynb
│   └── RAG_Gemini(QA-pair).ipynb
├── with pre-trained model (RAG with pre-trained model)
│   └── RAG_bloomz-1b7.ipynb
├── README.md
├── requirements.txt
└── create_vector_db.py (for creating a vector DB)
```

## Resources Used

- Python Version: 3.11.9
- IDE: VSCode
- Requirements:
  - Install [requirements](https://github.com/JohnnyHsieh1020/diabetic_RAG_QA/blob/main/requirements.txt)
    ```terminal
    pip install -r requirements.txt
    ```

## References

1. Articles:
   - https://www.tnhosp.mohw.gov.tw/warehouse/%7BCA7FF96E-F97E-40F6-9AEA-58993C05E61A%7D/%E7%B3%96%E5%B0%BF%E7%97%85%E8%BF%B7%E6%80%9D%E5%95%8F%E7%AD%94.pdf
   - https://blog.health2sync.com/the-tips-of-record-diet/
2. Sentence transformer:
   - https://huggingface.co/DMetaSoul/sbert-chinese-general-v2
3. Paper:
   - https://arxiv.org/abs/2405.13179v2 (for sorting the related content)
