import re

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета
    и возвращает строку с замаскированным номером"""

    if re.match(r"Счет", account_card):
        mask_account = "".join(re.findall(r"\d", account_card))
        return re.sub(r"\d{20}", get_mask_account(mask_account), account_card)
    else:
        mask_card = "".join(re.findall(r"\d", account_card))
        return re.sub(r"\d{16}", get_mask_card_number(mask_card), account_card)


def get_date(original_date: str) -> str:
    """Функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" ("11.03.2024")."""

    # Проверим, соответствует ли строка ожидаемому формату с регулярным выражением
    if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}", original_date):
        raise ValueError("Некорректный формат даты")

    date_split_list = original_date.split("T")
    formated_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", (date_split_list[0]))
    return formated_date
