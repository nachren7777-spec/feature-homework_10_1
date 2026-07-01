def get_mask_card_number(card_number_input: str = "") -> str:
    """Функция, которая маскирует номер карты."""
    check_int_card: bool = card_number_input.isdigit()
    if not check_int_card or len(card_number_input) != 16:
        return "Ошибка ввода номера карты"
    else:
        card_number_slice_1: str = card_number_input[0:4]
        card_number_slice_2: str = card_number_input[4:6]
        card_number_slice_3: str = "**"
        card_number_slice_4: str = "****"
        card_number_slice_5: str = card_number_input[13:]
        space: str = " "
        card_number_mask: str = (
            card_number_slice_1 + space
            + card_number_slice_2 + card_number_slice_3 + space
            + card_number_slice_4 + space
            + card_number_slice_5
        )
        return card_number_mask


def get_mask_account(mask_account_input: str = "") -> str:
    """Функция, которая маскирует номер банковского счета"""
    check_int_mask: bool = mask_account_input.isdigit()
    if not check_int_mask or len(mask_account_input) != 20:
        return "Ошибка ввода номера счета"
    else:
        mask_account_slice_1: str = "**"
        mask_account_slice_2: str = mask_account_input[16:]
        mask_account_mask: str = mask_account_slice_1 + mask_account_slice_2
        return mask_account_mask


"""Вызовы функций по умолчанию 1234567890123456 и 12345678901234567890"""
card_number: str = "1234567890123456"
mask_account: str = "12345678901234567890"

print(get_mask_card_number(card_number))
print(get_mask_account(mask_account))
