import pytest

from src.processing import filter_by_state, sort_by_date


# Параметризированные тесты для различных значений статуса
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]),
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]),
    ("PENDING", []),  # Проверка при отсутствии словарей с указанным статусом
])
def test_filter_by_state(transactions, state, expected):
    result = filter_by_state(transactions, state)
    assert result == expected

# Тесты для различных условий сортировки
@pytest.mark.parametrize("reverse_order, expected_ids", [
    (True, [1, 3, 4, 2]),  # Убывающий порядок с учетом сортировки по id для одинаковых дат
    (False, [2, 4, 1, 3])  # Возрастающий порядок
])
def test_sort_by_date_order(operations, reverse_order, expected_ids):
    sorted_operations = sort_by_date(operations, reverse_order)
    result_ids = [op["id"] for op in sorted_operations]
    assert result_ids == expected_ids

# Тесты на некорректные или нестандартные форматы дат
@pytest.mark.parametrize("invalid_date", [
    "2022-03-01",  # Неполный формат
    "01-03-2022T12:30:00.000000",  # Неправильный формат
    "not-a-date"  # Некорректная строка
])
def test_sort_by_date_invalid_format(operations, invalid_date):
    operations_with_invalid_date = operations + [
        {"id": 6, "date": invalid_date}
    ]
    with pytest.raises(ValueError):
        sort_by_date(operations_with_invalid_date)