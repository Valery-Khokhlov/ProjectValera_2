import os

from typing import List, Dict, Any

import pandas as pd


def read_csv_file(path_csv: str) -> List[Dict[str, Any]]:
    """
     Функция для считывания финансовых операций из CSV. Принимает путь к файлу CSV, в качестве аргумента,
    и выдает список словарей с транзакциями.
    """
    if not os.path.exists(path_csv):
        raise FileNotFoundError(f"Файл {path_csv} не найден.")

    try:
        df_csv = pd.read_csv(path_csv, sep=';')
        transactions_csv_list = df_csv.to_dict(orient="records")
    except pd.errors.ParserError as e:
        raise ValueError(f"Ошибка при чтении файла CSV: {e}")
    except Exception as e:
        raise Exception(f"Произошла непредвиденная ошибка: {e}")
    return transactions_csv_list


def read_excel_file(path_excel: str) -> List[Dict[str, Any]]:
    """
     Функция для считывания финансовых операций из Excel. Принимает путь к файлу Excel, в качестве аргумента,
    и выдает список словарей с транзакциями.
    """
    try:
        df_exl = pd.read_excel(path_excel)
        transactions_exl_list = df_exl.to_dict(orient="records")
    except ValueError as e:
        raise ValueError(f"Ошибка при чтении файла Excel: {e}")
    return transactions_exl_list
