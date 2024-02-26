import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('catalog.db')
    cur = base.cursor()
    if base:
        print('Всё кайф, братанчик')
    base.execute('CREATE TABLE IF NOT EXISTS catalog(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO catalog VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM catalog').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM catalog').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM catalog WHERE name == ?', (data,))
    base.commit()


async def filter_by_price_range(min_price, max_price):
    query = 'SELECT * FROM catalog WHERE CAST(price AS FLOAT) BETWEEN ? AND ?'
    params = (min_price, max_price)
    return cur.execute(query, params).fetchall()

def close_connection():
    cur.close()
    base.close()


