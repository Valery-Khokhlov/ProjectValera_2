import re

from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Возвращает список словарей с указанным значением ключа state"""
    filtered_list_of_transactions = []
    for value in transactions:
        if value["state"] == state:
            filtered_list_of_transactions.append(value)
    return filtered_list_of_transactions


def sort_by_date(operations: List[Dict], reduce: bool = True) -> List[Dict]:
    """
    Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате
    """
    for element in operations:
        if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}", element["data"]):
            raise ValueError("Некорректный формат даты")

    sorted_list_of_operations = sorted(operations, key=lambda x: x["date"], reverse=reduce)
    return sorted_list_of_operations
