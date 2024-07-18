# Official website of Priscilla FX

<p align="center">
    <img src="pics/1.png" alt="1"/>
</p>

[![License: GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg?style=for-the-badge)](LICENSE "License")
[![Donate](https://img.shields.io/badge/_-Donate-red.svg?logo=githubsponsors&labelColor=555555&style=for-the-badge)](https://boosty.to/priscilla-custom-effects "Donate")
[![Stars](https://img.shields.io/github/stars/masajinobe-ef/priscillafx-website?color=fff&labelColor=0C0E0F&style=for-the-badge)](https://boosty.to/priscilla-custom-effects "Stars")
[![Code Size](https://img.shields.io/github/languages/code-size/masajinobe-ef/priscillafx-website.svg?style=for-the-badge)](https://github.com/masajinobe-ef/priscillafx-website "Code Size")
[![Repository size](https://img.shields.io/github/repo-size/masajinobe-ef/priscillafx-website.svg?style=for-the-badge)](https://github.com/masajinobe-ef/priscillafx-website "Repository size")
[![Top language](https://img.shields.io/github/languages/top/masajinobe-ef/priscillafx-website.svg?style=for-the-badge)](https://github.com/masajinobe-ef/priscillafx-website "Top language")

## Описание

Официальный сайт Priscilla FX - платформа, созданная с использованием технологий для создания API.
Веб-сайт использует FastAPI в качестве серверной платформы.

### Сайт создан с использованием следующих технологий:

**Backend фреймворк:**

- **FastAPI** - Современный, высокопроизводительный веб-фреймворк для создания API.
- **FastAPI-Users** - Пакет для управления аутентификацией и регистрацией пользователей в приложениях FastAPI.

**База данных:**

- **Asyncpg** - Асинхронный интерфейс PostgreSQL.
- **SQLModel** - Предназначена для упрощения взаимодействия с базами данных SQL в приложениях FastAPI.
- **SQLAlchemy** - SQL-инструментарий и система объектно-реляционного отображения (ORM).
- **Alembic** - Инструмент миграции базы данных.

**Кэширование данных:**

- **FastAPI-Cache** - Пакет для кэширования с помощью Redis.
- **Redis** - Система хранения данных в памяти, используемая в качестве базы данных, кэша и брокера сообщений.

**Развёртывание приложения:**

- **Docker** - Платформа для разработки, доставки и запуска приложений в контейнерах.

Сайт имеет систему аутентификации пользователей с использованием **JSON Web Tokens (JWT)** и **cookie**.
Имеет систему миграции базы данных с помощью **Alembic**. Это позволяет легко управлять изменениями схемы базы данных.

<p align="center">
    <img src="pics/2.png" alt="2"/>
    <img src="pics/3.png" alt="3"/>
    <img src="pics/4.png" alt="4"/>
</p>

#### License

This project is licensed under GPL-3.0. Please refer to the [LICENSE](LICENSE) file for detailed license information.
