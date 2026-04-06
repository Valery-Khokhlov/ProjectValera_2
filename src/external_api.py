import os

import requests

from dotenv import load_dotenv

from utils import  read_json_file


# Загружаем переменную окружения
load_dotenv()

API_KEY = os.getenv("API_KEY")

def converting_amount_rubles(transaction: Dict) -> float:
    """
      Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
     Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли
    """
    for transaction in transactions_list:

        code_transaction = transaction['operationAmount']['currency']['code']

        if code_transaction == "RUB":
            return float(transaction['operationAmount']['amount'])

        elif code_transaction in ["USD", "EUR"]:
            to = "RUB"
            from_ = code_transaction
            amount = transaction['operationAmount']['amount']

            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)
            result = response.json()
            return float(result['result'])