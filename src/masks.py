from src.logging_config import setup_logging

# Импортируем и настраиваем логгер
logger = setup_logging('masks')


def get_mask_card_number(card_number: int | str) -> str:
    """Принимает номер карты и возвращает маску номера ХХХХ ХХ** **** ХХХХ."""

    card_number = str(card_number)

    if len(card_number) != 16:
        logger.error("Номер карты должен содержать 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    if not card_number.isdigit():
        logger.error("Номер карты должен содержать только цифры.")
        raise ValueError("Номер карты должен содержать только цифры.")

    formatted_number_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Карта отформатирована: {formatted_number_card}")
    return formatted_number_card


def get_mask_account(account_number: int | str) -> str:
    """Принимает номер счета и возврвщает маску номера **ХХХХ."""
    if not isinstance(account_number, str):
        account_number = str(account_number)

    if len(account_number) < 4:
        masked_account = "**" + account_number
        logger.info(f"Счёт отформатирован: {masked_account}")
        return masked_account
    else:
        masked_account = "**" + account_number[-4:]
        logger.info(f"Счёт отформатирован: {masked_account}")
        return masked_account
