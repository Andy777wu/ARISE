# 测试任务：T-02 数据库迁移验收

## 目标

验证 8 张 PostgreSQL 领域表、约束、索引、Alembic 升降级与默认分类初始化能力。

## 验收项

- [x] ORM 元数据包含 `users`、`family`、`family_member`、`category`、`asset`、`asset_snapshot`、`notification`、`verification_code` 八张表。
- [x] 金额精度、成员状态约束、快照级联删除、关键索引和唯一约束已由单元测试覆盖。
- [x] Alembic 离线升级 SQL 可生成，包含 8 张表的 PostgreSQL DDL。
- [x] 默认分类辅助函数可为指定家庭初始化银行存款、股票、基金。
- [x] 在空 PostgreSQL 16 数据库执行 `alembic upgrade head` 后检查建表，再执行 `alembic downgrade 20260818_0001` 验证回滚。

## 执行记录

2026-08-19：已通过 3 项单元测试、Ruff 和 Alembic 离线 SQL 验证；在临时 PostgreSQL 16 容器中实际升级后检测到 8 张领域表，降级至 `20260818_0001` 后检测到 0 张领域表。验收容器已删除。
