import os

from dotenv import load_dotenv


load_dotenv()

# Database onnection string
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# Redis connection string
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

# Secret JWT key
SECRET_AUTH = os.environ.get("SECRET_AUTH")
