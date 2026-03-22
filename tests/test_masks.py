import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризация теста
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


# Тест на исключение
@pytest.mark.parametrize(
    "invalid_card_number", ["123", "1234abcd5678efgh", ""]  # короткий номер  # символы  # пустая строка
)
def test_get_mask_card_number_invalid(invalid_card_number: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_card_number)
        assert str(exc_info.value) in ["Номер карты должен содержать 16 цифр."]


# Параметризация теста для get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [("12345678901234567890", "**7890"), ("00000000000000000000", "**0000")],  # корректный номер  # все нули
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


# Тест для проверки обработки некорректных данных
@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "123",  # числовой формат
        "",  # пустая строка
    ],
)
def test_get_mask_account_invalid(invalid_account_number: int | str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_account_number)
        assert str(exc_info.value) in ["Номер карты должен содержать 20 цифр."]
