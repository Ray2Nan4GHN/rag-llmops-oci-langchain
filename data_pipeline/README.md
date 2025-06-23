# data_pipeline

本目录包含原始文档的加载、切分、嵌入生成与索引构建模块。

## 子模块说明

- `ingest/`: 加载 PDF/HTML/Word 文档，并提取元数据
- `embedding/`: 调用 OpenAI / HuggingFace 等模型生成向量表示
- `index/`: 将嵌入数据写入向量数据库（如 Qdrant / Pinecone）

## 用法

```bash
python ingest/load_documents.py
python embedding/embed_texts.py
python index/vector_indexer.py
