from typing import List

"""Cловарь по умолчанию"""
default_dict: List[dict] = [
    {'id': 41428829, 'state': 'EXECUTED',
     'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED',
     'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED',
     'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED',
     'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(data: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """функция, которая возвращает значения по параметру state"""
    return [i for i in data if i['state'] == state]


def sort_by_date(data: List[dict], reverse: bool = True) -> List[dict]:
    """Сортирует список словарей по дате (ключ 'date')."""
    if reverse:
        sorted_list = sorted(data, key=lambda x: x['date'], reverse=True)
        return sorted_list
    else:
        sorted_list = sorted(data, key=lambda x: x['date'], reverse=False)
        return sorted_list


"""Переменная state, по умолчанию 'EXECUTED', """
state: str = "EXECUTED"
"""постоянное значение state 'EXECUTED"""
if not state:
    state = "EXECUTED"
if state != "EXECUTED" and state != "CANCELED":
    print([])

"""вызов функции filter_by_state"""
print(filter_by_state(default_dict, state))

"""Вызова функции sort_by_date"""
print(sort_by_date(default_dict))
