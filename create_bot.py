from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5645984976:AAElYx7OvosOzezB9BO28lqE0AsSdobRjfw')
dp = Dispatcher(bot, storage=storage)
