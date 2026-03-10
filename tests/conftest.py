import pytest

from typing import Dict, List, Union, Tuple


@pytest.fixture
def card_number() -> List[Tuple[str, str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),  # корректный номер
        ("0000000000000000", "0000 00** **** 0000"),  # все нули
    ]

@pytest.fixture
def account_number() -> List[Tuple[str, str]]:
    return [
        ("73654108430135874305", "**4305"), # корректный номер
        ("00000000000000000000", "**0000"), # все нули
    ]

@pytest.fixture
def transactions() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.fixture
def operations() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 1, "date": "2022-03-01T12:30:00.000000"},
        {"id": 2, "date": "2022-01-15T08:45:00.000000"},
        {"id": 3, "date": "2022-03-01T12:30:00.000000"},  # одинаковая дата
        {"id": 4, "date": "2022-02-20T09:15:00.000000"}
    ]

@pytest.fixture
def account_cards() -> List[Tuple[str, str]]:
    return [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589")
    ]

@pytest.fixture
def date_format() -> List[Tuple[str, str]]:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("Некорректная строка без даты", None)
    ]