from typing import Dict, Any

import os

import requests

import random

from dotenv import load_dotenv

from utils import  read_json_file


# Загружаем переменную окружения
load_dotenv()

API_KEY = os.getenv("API_KEY")

def converting_amount_rubles(transaction: Dict[str, Dict[str, Dict[str, Any]]]) -> float:
    """
      Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
     Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли
    """

    code_transaction = transaction['operationAmount']['currency']['code']

    if code_transaction == "RUB":
        return float(transaction['operationAmount']['amount'])

    elif code_transaction in ["USD", "EUR"]:
        to = "RUB"
        from_= code_transaction
        amount = transaction['operationAmount']['amount']

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            return float(result['result'])
        except requests.exceptions.HTTPError:
            print("HTTP Error. Please check the URL.")
            return  0.0
        except requests.exceptions.RequestException:
            print("An error occurred. Please try again later.")
            return 0.0