from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('режим работы 🕐')
b2 = KeyboardButton('расположение 🌎')
b3 = KeyboardButton('каталог товаров👟')
b4 = KeyboardButton('отзывы✔️')
b5 = KeyboardButton('как сделать заказ?💬')
b6 = KeyboardButton('контакты📞')
# b4 = KeyboardButton('/Загрузить')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить, где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1, b2).row(b3,b5).row(b4).row(b6)
