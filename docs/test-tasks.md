# 测试任务：T-01 脚手架验收

## 目标

验证 T-01 的前后端工程、环境配置、健康检查、迁移骨架与质量门禁符合验收标准。

## 验收项

- [x] 后端健康检查 `GET /api/v1/health` 返回统一响应结构和 `request_id`。
- [x] 前端开发服务器可通过 `/api` 将请求代理至后端。
- [x] 开发与生产环境的 API 地址配置可分别被 Vite 读取。
- [x] Alembic 迁移历史和离线生成 SQL 命令可运行；业务表迁移留待 T-02。
- [x] `pytest`、Ruff、ESLint、Prettier 与前端生产构建通过。

## 执行记录

已验收（2026-08-18）：后端 `pytest`、Ruff 与 Alembic 离线迁移命令通过；
前端 ESLint、Prettier 检查通过，`npm run build` 由人工执行并通过。
