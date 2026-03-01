from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Возвращает список словарей с указанным значением ключа state"""
    filter_transactions = []
    for value in transactions:
        if value["state"] == state:
            filter_transactions.append(value)
    return filter_transactions


def sort_by_date(transactions: List[Dict], reduce: bool = True) -> List[Dict]:
    """
    Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате
    """
    sort_transactions = sorted(transactions, key=lambda x: x["date"], reverse=reduce)
    return sort_transactions
