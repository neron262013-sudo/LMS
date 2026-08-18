from rest_framework.serializers import ValidationError


def validate_forbidden_links(value):
    # Приводим текст к нижнему регистру для надежности
    value_lower = value.lower()

    # Проверяем, есть ли в тексте ссылка (http, https или www)
    if "http" in value_lower or "www." in value_lower:

        # Если ссылка есть, но это не Ютуб - выдаем ошибку
        if "youtube.com" not in value_lower and "youtu.be" not in value_lower:
            raise ValidationError("Разрешены ссылки только на youtube.com")

    return value