import requests
from telegram import Update
from telegram.ext import CallbackContext
import keyboards
import db

# Telegram Bot API Token
from config import TOKEN
def start(update: Update, context: CallbackContext) -> None:
    db.add_user(user_id=update.message.chat_id, user_name=update.message.chat.first_name)
    update.message.reply_text("Assalomu aleykum!\nushbu bot sizga kelajak kasblarini o'rgatadi!",reply_markup=keyboards.home())
def dasturlash_tillari(update:Update,context:CallbackContext):
    db.add_user(user_id=update.message.chat_id,user_name=update.message.chat.first_name)
    update.message.reply_text("Dasturlash tillari",reply_markup=keyboards.home_keyboard())
def send_task(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    update.message.reply_text(db.task(user_id))
def English(update:Update,context:CallbackContext):
    user_id=update.message.chat_id
    update.message.reply_text("Ingliz tilini biz bilan o'rganing!",reply_markup=keyboards.English())
def Level(update:Update,context:CallbackContext):
    user_id=update.message.chat_id
    update.message.reply_text("Darajangizni tanlang 👇.", reply_markup=keyboards.Level())
# def get_level(update:Update,context:CallbackContext):
#     user_id=update.message.chat_id
#     update.message.reply_poll()
def get_level(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    questions = [
        {"question": "Sizning darajangizni tanlang:", "options": ["Boshlang'ich", "O'rtacha", "Yuqori"], "correct_option_id": 2},
        {"question": "Sizning yoshingizni tanlang:", "options": ["Past", "O'rtacha", "Yuqori"], "correct_option_id": 0}
    ]
    correct_answers = 0
    
    for question_data in questions:
        question = question_data["question"]
        options = question_data["options"]
        correct_option_id = question_data["correct_option_id"]
        
        context.bot.send_poll(
            chat_id=user_id,
            question=question,
            options=options,
            is_anonymous=False,
            allows_multiple_answers=False,
            correct_option_id=correct_option_id,
            explanation=f"To'g'ri javob: {options[correct_option_id]}\n\n"
                        f"Har bir to'g'ri javobni sanab borish uchun bu so'roqda "
                        f"{len(options)} ta variant mavjud.",
            explanation_parse_mode="MarkdownV2"
        )
        
        correct_answers += 1 if correct_option_id == 0 else 0
        
        # Noto'g'ri javobni belgilash uchun qizil ptichka yaratamiz
        context.bot.send_poll(
            chat_id=user_id,
            question="",
            options=["Noto'g'ri"],
            is_anonymous=False,
            allows_multiple_answers=False,
            explanation="Noto'g'ri javob",
            explanation_parse_mode="MarkdownV2"
        )
    
    # Oxirida nechta to'g'ri javob topgani aytish
    update.message.reply_text(f"Siz {correct_answers} ta savoldan to'g'ri javob topdingiz.")

def compile_cpp(update: Update, context: CallbackContext) -> None:
    code = update.message.text
    user_id = update.message.chat_id
    result = db.compile_cpp_code(code,user_id)
    update.message.reply_text(result)

def orqaga_level(update:Update, context: CallbackContext):
    user_id=update.message.text
    update.message.reply_text(reply_markup=keyboards.English())