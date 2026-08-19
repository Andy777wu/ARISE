import base64
import hashlib
import secrets
import string
from uuid import uuid4


def generate_code(length: int = 5) -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def digest(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def generate_captcha() -> tuple[str, str, str]:
    captcha_id = str(uuid4())
    code = generate_code()
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="140" height="48">'
        '<rect width="100%" height="100%" fill="#f5f5f5"/>'
        '<text x="18" y="34" font-size="28" font-family="monospace" '
        f'letter-spacing="6">{code}</text>'
        "</svg>"
    )
    return captcha_id, code, base64.b64encode(svg.encode()).decode()
