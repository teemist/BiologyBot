import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import keyboards, admin_id

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command

from aiogram import F

from config import TOKEN_API

# хардкод времен для записи на занятие
global freetime
freetime = ["15:00", "14:43", "16:00", "17:00"]

bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot)
router = Router()
dp.include_router(router)


async def on_startup(_):
    print('Старт работы бота')


@dp.message(Command('admin'))
async def admin_start(message: types.Message):
    if message.from_user.id == int(admin_id.ADMIN_ID):
        await message.delete()
        await bot.send_message(message.from_user.id, text=f"Привет, админ {message.from_user.first_name}",
                               reply_markup=keyboards.admin_kb)


@dp.callback_query(F.data == "edit_time")
async def callback_time_menu_kb(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text="Все доступные времена на запись",
                           reply_markup=update_time_admin_kb())


# обновление клавиатуры с временем для админа
def update_time_admin_kb():
    kb_ft = InlineKeyboardBuilder()
    for time in freetime:
        kb_ft.add(InlineKeyboardButton(text=f"{time}", callback_data=time + "1"))
    kb_ft.add(keyboards.regButtonLeave)
    return kb_ft.as_markup()


@dp.message(Command('start'))
async def start_answer(message: types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id, text="Меню записи на занятие", reply_markup=keyboards.random_kb)


@dp.callback_query(F.data == "reg")
async def callback_reg_menu_kb(callback_query: types.CallbackQuery):
    if callback_query.data == "reg":
        update_time_kb()
        await bot.send_message(callback_query.from_user.id, "Запись на занятие", reply_markup=keyboards.reg_keyboard)


@dp.callback_query(F.data == "leave")
async def callback_gotoreg_menu_kb(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text="Меню записи на занятие", reply_markup=keyboards.random_kb)


@dp.callback_query(F.data == "time")
async def callback_time_menu_kb(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text="Выберите свободное время",
                           reply_markup=update_time_kb())


@dp.callback_query()
async def callback_delete_time(callback_query: types.CallbackQuery):
    if callback_query.data.endswith("1"):
        if callback_query.data[:-1] in freetime:
            await bot.send_message(callback_query.from_user.id, text=str(freetime))
            freetime.remove(callback_query.data[:-1])
            update_time_kb()
            await bot.send_message(callback_query.from_user.id, text=f"Удалено {callback_query.data[:-1]}")
            await bot.send_message(callback_query.from_user.id, text=str(freetime))
    else:
        await bot.send_message(callback_query.from_user.id, callback_query.data + "из панели выбора")
        if callback_query.data in freetime:
            await bot.send_message(callback_query.from_user.id, text=str(freetime))
            freetime.remove(callback_query.data)
            update_time_kb()
            await bot.send_message(callback_query.from_user.id, text=f"Выбрано {callback_query.data}")
            await bot.send_message(callback_query.from_user.id, text=str(freetime))


# обновление клавиатуры с временем
def update_time_kb():
    kb_ft = InlineKeyboardBuilder()
    for time in freetime:
        kb_ft.add(InlineKeyboardButton(text=f"{time}", callback_data=time))
    kb_ft.add(keyboards.regButtonLeave)
    return kb_ft.as_markup()


# @dp.callback_query()
# async def callback_choosen_time(callback_query: types.CallbackQuery):
#     if not callback_query.data.endswith("1"):
#         await bot.send_message(callback_query.from_user.id, callback_query.data + "из панели выбора")
#         if callback_query.data in freetime:
#             await bot.send_message(callback_query.from_user.id, text=str(freetime))
#             freetime.remove(callback_query.data)
#             update_time_kb()
#             await bot.send_message(callback_query.from_user.id, text=f"Выбрано {callback_query.data}")
#             await bot.send_message(callback_query.from_user.id, text=str(freetime))


# @dp.callback_query(F.data == "tb1")
# async def callback_tb1_kb(callback_query: types.CallbackQuery):
#     # if F.data in freetime:
#     # freetime.remove(F.data)
#     await bot.send_message(callback_query.from_user.id, text="Вы успешно записаны на 15:00",
#                            reply_markup=keyboards.time_keyboard)
#     # F.data = None
#     await bot.send_message(callback_query.from_user.id, text="15:00")

class HomeworkState(StatesGroup):
    waiting_for_homework = State()


@dp.message(Command('hw'))
async def start_answer(message: types.Message, state: FSMContext):
    await message.delete()
    await bot.send_message(message.from_user.id, text="Меню для сдачи дз. Скинь сюда свое дз")
    await state.set_state(HomeworkState.waiting_for_homework)


@dp.message(HomeworkState.waiting_for_homework)
async def receive_homework(message: types.Message, state: FSMContext):
    # Пользователь отправил дз, завершаем состояние
    await state.clear()
    # Отправляем подтверждение получения
    await bot.send_message(message.from_user.id, text="Твое дз получено")
    await bot.forward_message(chat_id=-1002282232622, from_chat_id=message.chat.id, message_id=message.message_id)


@dp.message(Command('iddd'))
async def start_answer(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=str(message.chat.id))
    await message.delete()


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
