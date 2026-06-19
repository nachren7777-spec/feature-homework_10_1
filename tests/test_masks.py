import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize("card_number_input, expected", [
    ("123", "Ошибка ввода номера карты"),
    ("1235678901234567890", "Ошибка ввода номера карты"),
    ("ffffffffffffffff", "Ошибка ввода номера карты"),
    ("1234567890123456", "1234 56** **** 456"),
    ])

def test_get_mask_card_number(card_number_input:str, expected:str):
    assert get_mask_card_number(card_number_input) == expected

@pytest.mark.parametrize("mask_account_input, expected", [
    ("", "Ошибка ввода номера счета"),
    ("1", "Ошибка ввода номера счета"),
    ("123456789012345678901", "Ошибка ввода номера счета"),
    ("12345678901234567890", "**7890"),
    ])

def test_get_mask_account(mask_account_input:str, expected:str):
    assert get_mask_account(mask_account_input) == expected
