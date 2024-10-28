 # Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл hello.py в контейнер
COPY config.py /app/config.py
COPY messages.py /app/messages.py
COPY handlers.py /app/handlers.py
COPY keyboards.py /app/keyboards.py
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
# Устанавливаем зависимости, если есть файл requirements.txt
RUN pip install -r requirements.txt

# Команда по умолчанию при запуске контейнера
CMD ["python", "main.py"]

