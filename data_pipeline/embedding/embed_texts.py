##文本加载 + Chunk 切分 + 嵌入生成 + Qdrant 入库 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 加载本地文档
loader = TextLoader("sample_docs/example.txt")
docs = loader.load()

# Chunk 切分
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 嵌入生成与入库
embedding = OpenAIEmbeddings()
qdrant = Qdrant.from_documents(
    documents=chunks,
    embedding=embedding,
    url="http://localhost:6333",
    collection_name="rag_docs"
)
print("Documents embedded and stored in Qdrant.")
