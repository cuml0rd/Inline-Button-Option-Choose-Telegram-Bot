from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

def numbers(one_on: bool = False, two_on: bool = False, three_on: bool = False, four_on: bool = False):
    menu = InlineKeyboardMarkup(row_width=2)
    one = InlineKeyboardButton(
        '🌕 1' if one_on else '🌑 1', callback_data=f'type|1|{int(one_on)}')
    two = InlineKeyboardButton(
        '🌕 2' if two_on else '🌑 2', callback_data=f'type|2|{int(two_on)}')
    three = InlineKeyboardButton(
        '🌕 3' if three_on else '🌑 3', callback_data=f'type|3|{int(three_on)}')
    four = InlineKeyboardButton(
        '🌕 4' if four_on else '🌑 4', callback_data=f'type|4|{int(four_on)}')
    confirm = InlineKeyboardButton(
        'Confirm', callback_data='confirm')
    menu.row(one, two)
    menu.row(three, four)
    menu.add(confirm)
    return menu
