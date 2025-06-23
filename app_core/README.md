
### `app_core/README.md`

```markdown
# app_core

包含核心的 RAG 检索 + LLM 推理逻辑。

## 主要模块

- `query_handler.py`: 统一调用链，负责组装 Prompt → 调用模型
- `retriever_chain.py`: 封装向量检索逻辑
- `prompt_templates/`: 存储 Jinja2 Prompt 模板
- `llm_caller.py`: 对接 OpenAI、Bedrock、Azure 模型

适用于 LangChain / LlamaIndex 的封装方式，支持快速替换模型与 Prompt。
