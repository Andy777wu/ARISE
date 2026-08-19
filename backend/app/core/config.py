from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://arise:arise@localhost:5432/arise"
    cors_origins: str = "http://localhost:5173"
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = "replace-me-in-production"
    token_expire_seconds: int = 86400
    captcha_expire_seconds: int = 300
    code_expire_seconds: int = 300
    code_send_interval_seconds: int = 60
    code_daily_limit: int = 10
    login_failure_limit: int = 5
    login_lock_seconds: int = 900
    login_ip_limit_per_minute: int = 20
    auth_delivery_mode: str = "console"
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_from: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_prefix="ARISE_", extra="ignore")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
