from typing import List, Dict, Generator

def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """
    Фильтрует операции по заданной валюте.

    Args:
        transactions (List[Dict]): Список операций.
        currency (str): Валюта для фильтрации.

    Yields:
        Dict: Операции, соответствующие заданной валюте.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction

def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генерирует описания операций.

    Args:
        transactions (List[Dict]): Список операций.

    Yields:
        str: Описание операции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")

def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start (int): Начальный номер.
        end (int): Конечный номер.

    Yields:
        str: Номер банковской карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for num in range(start, end + 1):
        yield f"{num:016}".replace("", " ")[1:-1]
