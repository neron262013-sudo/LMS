from urllib.parse import urlparse

from rest_framework.serializers import ValidationError


def validate_forbidden_links(value: str) -> str:
    for word in value.split():
        if word.startswith(("http://", "https://", "www.")):
            url = word if "://" in word else f"https://{word}"
            hostname = (urlparse(url).hostname or "").lower()
            allowed = hostname == "youtube.com" or hostname.endswith(".youtube.com") or hostname == "youtu.be"
            if not allowed:
                raise ValidationError("Разрешены ссылки только на YouTube")
    return value
