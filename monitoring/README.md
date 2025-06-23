#  monitoring

全链路追踪与性能监控模块。

## 功能说明

- `tracing/`: 记录检索、Prompt、生成等链路日志
- `metrics/`: 暴露给 Prometheus / Grafana 的系统指标

可接入 LangSmith、Datadog、OpenTelemetry。
