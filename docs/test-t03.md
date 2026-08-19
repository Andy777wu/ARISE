# 测试任务：T-03 认证体系验收

## 验收结果

- [x] 图片验证码接口返回 SVG Base64 数据。
- [x] 验证码仅以 SHA-256 哈希写入 Redis 和审计表，5 分钟有效。
- [x] 单元测试覆盖 60 秒发送间隔和连续 5 次失败锁定 15 分钟。
- [x] Docker Compose 集成验证：首次验证码登录自动创建用户，`/auth/me` 成功，新登录后旧 Token 返回 `4002`。
- [x] 后端 Pytest、Ruff 和前端 ESLint、Prettier、生产构建通过。

## 投递说明

本地使用 `ARISE_AUTH_DELIVERY_MODE=console`，验证码写入后端服务日志；生产邮件可将模式切换为 `smtp` 并设置 `ARISE_SMTP_*`。阿里云短信凭据待配置后接入。
