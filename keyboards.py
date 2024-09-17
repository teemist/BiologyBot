from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Объект клавиатуры (пример создания клавы)
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         keyboard=[[KeyboardButton(text="/help"), KeyboardButton(text="/description"),
                                    KeyboardButton(text="/give"), KeyboardButton(text="/picture"),
                                    KeyboardButton(text="/inline")]])

# объект inline клавиатуры (пример создания клавы, прикрепленной к сообщению от бота)
ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="google", url="google.com"),
                                             InlineKeyboardButton(text="facebook", url="facebook.com")]])
