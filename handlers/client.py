from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client
from data_base import sqlite_db
from aiogram. types import InlineKeyboardMarkup, InlineKeyboardButton

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет!🍀', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/megekbot')

# @dp.message_handler(commands=['Режим_работы'])

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='VK', url='https://vk.com/memphis.logistics')
urlButton2 = InlineKeyboardButton(text='Telegram ', url='https://t.me/memphis_store')
urlkb.add(urlButton, urlButton2)

#dp.message handler (commands="ссылки")
async def url_command (message : types .Message):
    await message.answer ( "наши группы в:", reply_markup=urlkb)

async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'пн-пт с 12 до 19')

# @dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Романов переулок, 4с2')

# @dp.message_handler(commands=['Каталог_товаров'])
async def command_catalog(message: types.Message):
   await sqlite_db.sql_read(message)


async def info(message: types.Message):
    await bot.send_message(message.from_user.id, 'отзывы о работе с нами\n•https://vk.com/shreckx?w=wall248557604_557%2Fall')

#@dp.message_handlers(lambda message: "как" in message.text)
async def order(message: types.Message):
    await bot.send_message(message.from_user.id, '1)выберете товар из нашего каталога\n2)напишите нашему менеджеру @Dsdo7')


# Функция фильтрации по цене
#@dp.message_handler(commands=['filter_price'])
async def filter_price(message: types.Message):
    try:
        await message.reply('Введите минимальную и максимальную цены в формате "минимальная_цена максимальная_цена":')
        await dp.register_next_step_handler(message, process_price_range)
    except Exception as e:
        await message.reply('Что-то пошло не так: ' + str(e))


async def process_price_range(message: types.Message):
    try:
        price_range = message.text.split()
        if len(price_range) != 2:
            await message.reply('Некорректный формат ввода. Введите минимальную и максимальную цены через пробел.')
            return

        min_price = float(price_range[0])
        max_price = float(price_range[1])

        results = await sqlite_db.filter_by_price_range(min_price, max_price)

        if results:
            for ret in results:
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
        else:
            await message.reply('Товары не найдены')
    except ValueError:
        await message.reply('Некорректный формат цены')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(url_command, lambda message: "контакты" in message.text)
    dp.register_message_handler(open_command, lambda message: "режим" in message.text)
    dp.register_message_handler(place_command, lambda message: "расположение" in message.text)
    dp.register_message_handler(command_catalog, lambda message: "каталог" in message.text)
    dp.register_message_handler(info, lambda message: "отзывы" in message.text)
    dp.register_message_handler(order, lambda message: "как" in message.text)
    dp.register_message_handler(filter_price, lambda message: "фильтр" in message.text)
    #commands=['как_сделать_заказ']