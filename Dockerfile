 # ���������� ������� ����� Python
FROM python:3.9-slim

# ������������� ������� ����������
WORKDIR /app

# �������� ���� hello.py � ���������
COPY config.py /app/config.py
COPY messages.py /app/messages.py
COPY handlers.py /app/handlers.py
COPY keyboards.py /app/keyboards.py
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
# ������������� �����������, ���� ���� ���� requirements.txt
RUN pip install -r requirements.txt

# ������� �� ��������� ��� ������� ����������
CMD ["python", "main.py"]

