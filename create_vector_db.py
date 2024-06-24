# Packages
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# External data(Article)
EXTERNAL_DATA_PATH = "./doc/diabetic_acticles.pdf"

# External data(QA)
# EXTERNAL_DATA_PATH = "./doc/diabetic_qa.pdf"

# Sentence embedding
EMBED_MODEL_NAME = "DMetaSoul/sbert-chinese-general-v2"
# ----------------------------------------------------------------

# Load external data
print("Loading external data...")
loader = PyPDFLoader(EXTERNAL_DATA_PATH)
content = loader.load()
print("Done loading external data!\n")
print(content)
# ----------------------------------------------------------------

# Split external data(Article)
print("Splitting external data...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=150,
    keep_separator=False,
    separators=["\u3002", "\uff0c", "\n"],  # 。  # ，
)
# Split external data(QA)
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=50,
#     chunk_overlap=0,
#     keep_separator=False,
#     separators=["#"]
# )
all_splits = text_splitter.split_documents(content)
print(all_splits)
print("Done splitting external data!\n")
# ----------------------------------------------------------------

# Embedding all_splits
# Change to "cpu" or "cuda" if your machine is Windows.
model_kwargs = {"device": "mps"}
embedding = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL_NAME, model_kwargs=model_kwargs
)

print("Embedding all splits and store to Vector DB...")
db = FAISS.from_documents(all_splits, embedding)
# ----------------------------------------------------------------

# Save in FAISS vector DB(article)
db.save_local("diabetic_vector_db")

# Save in FAISS vector DB(QA)
# db.save_local("diabetic_qa_vector_db")
print("Done embedding and saved as vector DB!")
