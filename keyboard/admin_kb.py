from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# кнопки клавиатуры админа
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)

button_case_admin.add(button_load, button_delete)
