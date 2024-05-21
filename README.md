# Banking Operations Widget

Этот проект содержит функции для фильтрации и сортировки списка банковских операций.

## Установка зависимостей

Для установки зависимостей используйте Poetry:

```bash
poetry install
```

## Тестирование

Проект покрыт тестами с использованием библиотеки `pytest`. Для запуска тестов выполните команду:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```
## Новые функции

### Генераторы для обработки транзакций

#### filter_by_currency

Функция `filter_by_currency` принимает список транзакций и фильтрует их по заданной валюте.

Пример использования:

python
usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(3):
    print(next(usd_transactions)["id"])
