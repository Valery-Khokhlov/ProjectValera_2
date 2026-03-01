def filter_by_state(list_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список словарей с указанным значением ключа state"""
    filter_lists = []
    for dictionary in list_state:
        if dictionary["state"] == state:
            filter_lists.append(dictionary)
    return filter_lists


def sort_by_date(list_dict: list[dict], reduce: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=reduce)
    return sorted_list
