# Телеграмм Бот

Этот проект представляет собой простого телеграмм бота, написанного на Python с использованием библиотеки aiogram. 
Бот предоставляет различные функции, такие как управление каталогом товаров, отправка контактных данных и другие.

Структура проекта
main.py: Точка входа в приложение, где настраивается бот и запускаются обработчики.
create_bot.py: Модуль для создания объектов бота и диспетчера.
handlers/: Директория содержит модули с обработчиками команд и сообщений.
data_base/: Директория содержит модуль для работы с базой данных SQLite.
keyboard/: Директория содержит модули с клавиатурами для бота.
bot_run.bat: Файл для запуска бота в Windows.

Для запуска кода нужно создать файл bot_run.bat в той же директории, что и telebot, содержащий следующее:
'''
@echo off

call %~dp0telebot\venv\Scripts\activate

cd %~dp0telebot

set TOKEN="ваш токен"

python main.py

pause
'''
