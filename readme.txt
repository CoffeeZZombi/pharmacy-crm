# Pharmacy CRM

CRM-система для управления аптекой, разработанная с использованием FastAPI и MySQL. Подходит для учёта клиентов, товаров, остатков и продаж.

## Возможности

- Управление клиентами
- Управление товарами
- Учёт продаж
- Учёт остатков на складе

## Стек технологий

- **Язык:** Python 3.10+
- **Фреймворк:** FastAPI
- **База данных:** MySQL
- **ORM:** SQLAlchemy
- **Схемы данных:** Pydantic

## Структура проекта

pharmacy-crm/
├── app/
│ ├── crud/ # Логика операций с БД
│ ├── models/ # SQLAlchemy модели
│ ├── routers/ # FastAPI маршруты
│ ├── schemas/ # Pydantic схемы
│ └── database.py # Подключение к базе данных
├── main.py # Точка входа
├── requirements.txt # Зависимости проекта
└── README.md

## Установка и запуск

 Клонируй репозиторий:
git clone https://github.com/твоя-ссылка/pharmacy-crm.git
cd pharmacy-crm

Установи зависимости:
pip install -r requirements.txt


Настрой подключение в app/database.py:
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://pharmacy_user:Zasada98666@localhost/pharmacy_db"

Запусти сервер:
uvicorn main:app --reload

Перейди в браузере:
http://127.0.0.1:8000/docs