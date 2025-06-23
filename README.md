项目架构

rag-llmops-system/  
│  
├──  data_pipeline/                     # 文档处理与向量生成管道  
│   ├── ingest/  
│   │   ├── load_documents.py            # 文档加载器（PDF, HTML, etc.）  
│   │   ├── chunk_documents.py           # 文档 Chunk 切分器  
│   │   └── metadata_extractor.py        # 提取文档元数据  
│   ├── embedding/. 
│   │   ├── embed_texts.py               # 调用 Embedding API 生成向量  
│   │   ├── embedding_registry.py        # 嵌入模型注册与版本管理  
│   │   └── embedding_config.yaml        # 嵌入配置文件（模型/维度等）  
│   └── index/  
│       ├── vector_indexer.py            # 向量入库操作  
│       ├── index_snapshot.py            # 向量库快照管理  
│       └── retriever_interface.py       # 检索接口封装  
│  
├──  app_core/                          # 核心 RAG 应用逻辑  
│   ├── query_handler.py                 # 用户查询统一入口  
│   ├── retriever_chain.py               # 向量检索链逻辑  
│   ├── prompt_templates/  
│   │   ├── default_prompt.jinja         # Prompt 模板（支持版本控制）  
│   │   └── prompt_registry.py           # Prompt 模板注册/加载器  
│   ├── llm_caller.py                    # LLM 接口封装（支持多模型）  
│   └── response_formatter.py            # 格式化输出结构（含来源）  
│  
├──  monitoring/                        # 监控与跟踪系统   
│   ├── tracing/  
│   │   ├── session_tracer.py            # 生成 trace_id，记录全链路  
│   │   ├── retriever_logger.py          # 检索性能与命中日志  
│   │   ├── prompt_logger.py             # Prompt 使用日志  
│   │   └── output_logger.py             # 模型响应监控（含token用量）  
│   └── metrics/  
│       ├── grafana_dashboard.json       # 可视化看板配置示例  
│       └── prometheus_exporter.py       # 指标导出服务  
│  
├──  evaluation/                        # 自动化评估与反馈模块  
│   ├── ragas_runner.py                  # 基于 RAGAS 的自动评分  
│   ├── feedback_collector.py            # 前端/API 收集用户反馈  
│   ├── feedback_db/  
│   │   └── schema.sql                   # Feedback 数据库建表结构  
│   └── evaluation_reporter.py           # 汇总评估报告/可视化  
│  
├──  config/                           # 全局配置  
│   ├── app_config.yaml                  # 应用全局参数（端口、路径等）  
│   ├── llm_config.yaml                  # 模型调用配置  
│   └── vectorstore_config.yaml          # 向量库连接配置  
│  
├──  api_server/                        # API 与 Web 服务  
│   ├── main.py                          # FastAPI 入口  
│   ├── routes/  
│   │   ├── query_api.py                 # 提问接口（RAG 调用）  
│   │   ├── feedback_api.py              # 用户反馈提交接口  
│   │   └── healthcheck.py               # 系统健康检查  
│   └── middleware/  
│       └── tracing_middleware.py        # 统一 trace_id 注入  
│  
├──  ui_frontend/                       # 可选：前端 UI（聊天+反馈）  
│   ├── pages/  
│   ├── components/  
│   └── api/. 
│  
├──  scripts/                           # 常用维护脚本  
│   ├── update_embedding.sh              # 重建嵌入  
│   ├── clear_cache.sh                   # 清理缓存/旧日志  
│   └── export_logs.py                   # 日志导出工具  
│  
├── Dockerfile                           # 容器化支持  
├── docker-compose.yaml                  # 快速本地部署方案  
├── requirements.txt                     # Python 依赖  
└── README.md                            # 项目说明文档  
