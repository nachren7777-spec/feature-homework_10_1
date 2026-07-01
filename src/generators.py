from typing import List
from typing import Dict
from typing import Any
from typing import Generator

"""Неизменяемые данные"""
SPACE: str = " "

default_dictionary = [
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

global_beginning = 9999999999999997
global_end = 10000000000000000


def filter_by_currency(default_dictionary: List[dict], key: str) -> Generator[dict, None, None]:
    for transaction in default_dictionary:
        operation_amount = transaction.get("operationAmount")
        if operation_amount:
            currency_info = operation_amount.get("currency")
            if currency_info and currency_info.get("code") == key:
                yield transaction


key = "USD"

try:
    filtered_list = filter_by_currency(default_dictionary, key)
    print(next(filtered_list))
except StopIteration:
    print([])

for transaction in filter_by_currency(default_dictionary, key):
    print(transaction)


def transaction_descriptions(
    default_dictionary: List[Dict[str, Any]]
) -> Generator[str, None, None]:
    for transaction in default_dictionary:
        description = transaction.get("description")
        if description:
            yield description


for description in transaction_descriptions(default_dictionary):
    print(description)


def card_number_generator(beginning: int, end: int) -> Generator[str, None, None]:
    """
    Проверка, является ли переменные числами
    Не содежат пустую строку
    """
    if not isinstance(beginning, int) or not isinstance(end, int):
        return
    if beginning == "" or end == "":
        return
    if beginning < 1 or end > 10000000000000000 or beginning >= end:
        return
    """
    Генерирует номера карт в заданном диапазоне.
    Каждый номер - 16-значная строка с ведущими нулями.
    """
    try:
        number_generator = (
            str(10000000000000000 + num)[1:5] + SPACE
            + str(10000000000000000 + num)[5:9] + SPACE
            + str(10000000000000000 + num)[9:13] + SPACE
            + str(10000000000000000 + num)[13:]
            for num in range(beginning, end)
        )
    except TypeError:
        return
    for number in number_generator:
        yield number


for card in card_number_generator(global_beginning, global_end):
    print(card)
