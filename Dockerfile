FROM python:3.10

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]