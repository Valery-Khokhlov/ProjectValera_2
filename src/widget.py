import re

from black.strings import Match

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

    match: Match[str] | None = re.search(r"(\d{4})-(\d{2})-(\d{2})", original_date)
    return f"{match.group(3)}.{match.group(2)}.{match.group(1)}"
