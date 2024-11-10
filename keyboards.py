from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from main import freetime, main
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardBuilder

# Объект клавиатуры (пример создания клавы)
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         keyboard=[[KeyboardButton(text="/help"), KeyboardButton(text="/description"),
                                    KeyboardButton(text="/give"), KeyboardButton(text="/picture"),
                                    KeyboardButton(text="/inline")]])

# объект inline клавиатуры (пример создания клавы, прикрепленной к сообщению от бота)
ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="google", url="google.com"),
                                             InlineKeyboardButton(text="facebook", url="facebook.com")]])

vote_b1 = InlineKeyboardButton(text='🆗', callback_data="ok")
vote_b2 = InlineKeyboardButton(text='❤️', callback_data="like")
vote_keyboard = InlineKeyboardMarkup(inline_keyboard=[[vote_b1, vote_b2]])

# клавиатура для перелистывания случайных картинок
random_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="➡️", callback_data="reg")]])

# инлайн клавиатура для записи на занятие
regButton1 = InlineKeyboardButton(text='Записаться на занятие', callback_data="time")
regButtonLeave = InlineKeyboardButton(text='Выйти из меню❤️', callback_data="leave")
reg_keyboard = InlineKeyboardMarkup(inline_keyboard=[[regButton1, regButtonLeave]])

# инлайн клавиатура для выбора времени записи на занятие
# timeButton1 = InlineKeyboardButton(text='15:00', callback_data="tb1")
# timeButton2 = InlineKeyboardButton(text='16:00', callback_data="tb2")
# timeButton3 = InlineKeyboardButton(text='17:00', callback_data="tb3")
# regButtonLeave = InlineKeyboardButton(text='Выйти из меню❤️', callback_data="leave")
#
# time_keyboard = InlineKeyboardMarkup(inline_keyboard=[[timeButton1, timeButton2, timeButton3], [regButtonLeave]])

# клавиатура администратора

adminPanelLeave1 = InlineKeyboardButton(text='Выйти из меню❤️', callback_data="leave")
adminButtonEditTime = InlineKeyboardButton(text='Отредактировать время', callback_data="edit_time")


admin_kb = InlineKeyboardMarkup(inline_keyboard=[[adminButtonEditTime, adminPanelLeave1]])


