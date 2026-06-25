import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from typing import List, Dict, Any


@pytest.fixture
def def_default_dict() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


@pytest.mark.parametrize(
    "key, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188"
                }
            ]
        ),
        ("RUB", []),
        ("", []),
    ]
)
def test_filter_by_currency(key: str, expected: str, def_default_dict: List[dict]) -> None:
    result = list(filter_by_currency(def_default_dict, key))
    assert result == expected


@pytest.mark.parametrize(
    "transactions, expected_result",
    [
        (
            [
                {
                    "id": 939719570,
                    "description": "Перевод организации",
                },
                {
                    "id": 142264268,
                    "description": "Перевод со счета на счет",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions: List[dict], expected_result: List[dict]) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected_result


@pytest.mark.parametrize(
    "beginning, end, expected_numbers",
    [
        (
            1,
            3,
            ["0000 0000 0000 0001", "0000 0000 0000 0002"],
        ),
        (
            10009,
            10011,
            ["0000 0000 0001 0009", "0000 0000 0001 0010"],
        ),
        (
            9999999999999997,
            10000000000000000,
            [
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (10000000000000000, 100000000000000010, []),
        ("", "", []),
        (12, 10, []),
        (0, 10, []),
    ],
)
def test_card_number_generator(beginning: int, end: int, expected_numbers: List[str]) -> None:
    gen = card_number_generator(beginning, end)
    result = list(gen)
    assert result == expected_numbers
