"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

import smtplib
from email.message import EmailMessage

# Config
from config import (
    SMTP_HOST,
    SMTP_PORT,
    SMTP_PASSWORD,
    SMTP_USER,
    REDIS_HOST,
    REDIS_PORT,
)

# Celery
from celery import Celery


celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def get_email_template(username: str):
    email = EmailMessage()
    email['Subject'] = 'Hi!'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}! Добро пожаловать на сайт ШИЗОФРЕНИЯ! шизофрения.. шизофрения...</h1>'
        '<img src="https://priscilla-custom-effects.github.io/img/items/OD-820.jpg>'
        '</div>',
        subtype='html',
    )
    return email


@celery.task
def send_email_report_hello(username: str):
    try:
        email = get_email_template(username)
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(email)

    except Exception as e:
        print(e)
