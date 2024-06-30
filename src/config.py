"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

import os
from dotenv import load_dotenv


load_dotenv()

# Database onnection string
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
DB_NAME = os.environ.get('POSTGRES_NAME')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASS')
ECHO = os.environ.get('ECHO')

# Redis connection string
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

# Email
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')

# Secret JWT key
SECRET_AUTH = os.environ.get('SECRET_AUTH')
