import re

from pydantic import BaseModel, field_validator

PHONE_PATTERN = re.compile(r"^1\d{10}$")
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


class ContactRequest(BaseModel):
    contact: str

    @field_validator("contact")
    @classmethod
    def validate_contact(cls, value: str) -> str:
        value = value.strip().lower()
        if not (PHONE_PATTERN.fullmatch(value) or EMAIL_PATTERN.fullmatch(value)):
            raise ValueError("请输入有效的中国大陆手机号或邮箱")
        return value

    @property
    def is_email(self) -> bool:
        return bool(EMAIL_PATTERN.fullmatch(self.contact))


class SendCodeRequest(ContactRequest):
    captcha_id: str
    captcha_code: str


class LoginRequest(ContactRequest):
    code: str


class UserData(BaseModel):
    id: int
    phone: str | None
    email: str | None


class LoginData(BaseModel):
    token: str
    expires_in: int
    user: UserData
    is_new_user: bool
