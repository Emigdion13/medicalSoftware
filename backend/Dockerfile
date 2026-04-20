FROM python:3.11-slim

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh

CMD ["./wait-for-db.sh"]
