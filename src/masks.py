def get_mask_card_number(card_number: int | str) -> str:
    """Принимает номер карты и возвращает маску номера ХХХХ ХХ** **** ХХХХ."""

    card_number = str(card_number)

    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return str(f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")


def get_mask_account(account: int | str) -> str:
    """Принимает номер счета и возврвщает маску номера **ХХХХ."""

    account = str(account)

    if len(account) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр.")
    return str(f"**{account[-4:]}")
