import requests
from telegram import Update
from telegram.ext import CallbackContext
import keyboards
import db

# Telegram Bot API Token
from config import TOKEN
def start(update: Update, context: CallbackContext) -> None:
    db.add_user(user_id=update.message.chat_id, user_name=update.message.chat.first_name)
    update.message.reply_text("Assalomu aleykum!\nushbu bot sizga C++ dan berilgan topshiriqlarni bajarish uchun yordam beradi",reply_markup=keyboards.home_keyboard())

def send_task(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    update.message.reply_text(db.task(user_id))

def compile_cpp(update: Update, context: CallbackContext) -> None:
    code = update.message.text
    user_id = update.message.chat_id
    result = db.compile_cpp_code(code,user_id)
    update.message.reply_text(result)

