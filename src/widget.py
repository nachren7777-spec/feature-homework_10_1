"""Неизменяемые данные"""
SPACE: str = " "


def mask_account_card(number_card_or_account: str) -> str:
    """Функция, которая маскирует номер карты или счёта."""
    if len(number_card_or_account) <= 20:
        """Защита от неправильного ввода - короткий ввод текста"""
        return "Ошибка ввода номера карты"
    """Проверка на счёт"""
    check_account: str = number_card_or_account[-20:]
    check_account_bool: bool = check_account.isdigit()
    if check_account_bool:
        """Маскировка счёта"""
        account_str: str = number_card_or_account[:-20]
        mask_account_slice_1: str = "**"
        mask_account_slice_2: str = check_account[16:]
        mask_account_mask: str = (
            account_str + SPACE
            + mask_account_slice_1
            + mask_account_slice_2
        )
        return mask_account_mask
    """Проверка на карту"""
    check_card: str = number_card_or_account[-16:]
    check_card_bool: bool = check_card.isdigit()
    if check_card_bool:
        """Маскировка карты"""
        card_str: str = number_card_or_account[:-16]
        card_number_slice_1: str = check_card[0:4]
        card_number_slice_2: str = check_card[4:6]
        card_number_slice_3: str = "**"
        card_number_slice_4: str = "****"
        card_number_slice_5: str = check_card[13:]
        card_number_mask: str = (
            card_str + SPACE
            + card_number_slice_1 + SPACE
            + card_number_slice_2 + card_number_slice_3 + SPACE
            + card_number_slice_4 + SPACE
            + card_number_slice_5
        )
        return card_number_mask
    else:
        """Затычка, чтобы не ругался mypy"""
        return "Ошибка ввода номера карты"


def get_date(date_input: str) -> str:
    """Функция, которая принимает строку, а возвращает дату."""
    if len(date_input) != 10:
        return "Ошибка ввода даты"
    if date_input[2] == "." and date_input[5] == ".":
        return date_input
    for str_sim in date_input:
        if (
            str_sim != "1"
            and str_sim != "2"
            and str_sim != "3"
            and str_sim != "4"
            and str_sim != "5"
            and str_sim != "6"
            and str_sim != "7"
            and str_sim != "8"
            and str_sim != "9"
            and str_sim != "0"
            and str_sim != "."
        ):
            return "Ошибка ввода даты"
    year_date_input: str = date_input[0:4]
    month_date_input: str = date_input[5:7]
    day_date_input: str = date_input[8:10]
    dot: str = "."
    date_result: str = (
        day_date_input + dot
        + month_date_input + dot
        + year_date_input
    )
    return date_result


"""Вызовы функций по умолчанию Maestro 7000792289606361 и 2003.07.25"""
mask_account_or_card_number: str = "Maestro 7000792289606361"
print(mask_account_card(mask_account_or_card_number))

get_date_input: str = "2003.07.25"
print(get_date(get_date_input))
