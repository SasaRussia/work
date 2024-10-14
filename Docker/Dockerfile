 # Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл hello.py в контейнер
COPY hello.py .

# Устанавливаем зависимости, если есть файл requirements.txt
# RUN pip install -r requirements.txt

# Команда по умолчанию при запуске контейнера
CMD ["python", "hello.py"]

