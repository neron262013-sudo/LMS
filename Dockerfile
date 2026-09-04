# Указываем базовый образ
FROM python:3.14-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Обновляем список доступных пакетов,
# устанавливаем компилятор C и библиотеки PostgreSQL
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# gcc — компилятор C, необходимый для сборки некоторых Python-пакетов
# libpq-dev — файлы разработки PostgreSQL, необходимые для psycopg
# apt-get clean — очищаем кэш скачанных пакетов
# rm -rf /var/lib/apt/lists/* — удаляем списки пакетов,
# чтобы уменьшить размер Docker-образа

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Создаем директорию для медиа
RUN mkdir -p /app/media

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
