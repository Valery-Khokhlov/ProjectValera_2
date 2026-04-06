import json



def read_json_file(file_path: str) -> list:
    """
      Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []

transactions = read_json_file('data/operations.json')