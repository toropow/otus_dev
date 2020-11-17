import os

PG_HOST = os.environ.get('PG_HOST', '127.0.0.1')

SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://user:password@{PG_HOST}:5432/demo"