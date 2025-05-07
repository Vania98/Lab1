# Flask Cloud DB Example

Цей застосунок демонструє збереження даних у хмарній PostgreSQL базі через Flask.

## Запуск локально
```
pip install -r requirements.txt
export DATABASE_URL=postgresql://user:pass@host:port/dbname
python app.py
```

## Деплой на Render
1. Створіть нову PostgreSQL базу.
2. Створіть новий Web Service з цим репозиторієм.
3. Додайте змінну середовища `DATABASE_URL`.
