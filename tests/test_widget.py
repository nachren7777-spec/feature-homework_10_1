import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize("number_card_or_account, expected", [
    ("123", "Ошибка ввода номера карты"),
    ("ffffffffffffffffffff", "Ошибка ввода номера карты"),
    ("Счет 73654108430135874305", "Счет  **4305"),
    ("1234567890123456789", "Ошибка ввода номера карты"),
    ("12345678901234567890", "Ошибка ввода номера карты"),
    ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 361"),
    ("Maestro 7000792289606361", "Maestro  7000 79** **** 361")
])
def test_mask_account_card(number_card_or_account: str, expected: str) -> None:
    assert mask_account_card(number_card_or_account) == expected


@pytest.mark.parametrize("date_input, expected", [
    ("123", "Ошибка ввода даты"),
    ("2003.07.25", "25.07.2003"),
    ("25.07.2003", "25.07.2003"),
    ("1234567890123456789", "Ошибка ввода даты"),
    ("ffffffffff", "Ошибка ввода даты"),
    ("", "Ошибка ввода даты"),
])
def test_get_date(date_input: str, expected: str) -> None:
    assert get_date(date_input) == expected
