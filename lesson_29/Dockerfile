FROM python:3.14

COPY . /app

WORKDIR /app

RUN pip install psycopg2-binary pytest

ENV PYTHONPATH=/app

CMD ["python", "db_connection.py"]