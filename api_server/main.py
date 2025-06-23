
##基于 FastAPI + LangChain 的查询接口示例，接入 OpenAI + Qdrant 检索链
from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
import os

app = FastAPI()

# 初始化向量库和 LLM
embedding = OpenAIEmbeddings()
qdrant = Qdrant(
    url=os.getenv("VECTOR_DB_URL", "http://localhost:6333"),
    embeddings=embedding,
    collection_name="rag_docs"
)
retriever = qdrant.as_retriever()
llm = ChatOpenAI(temperature=0.3)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_rag(request: QueryRequest):
    result = qa_chain(request.query)
    return {
        "answer": result["result"],
        "source_documents": [doc.page_content for doc in result["source_documents"]]
    }
