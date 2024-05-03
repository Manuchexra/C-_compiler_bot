from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import db
def home():
    keyboard=ReplyKeyboardMarkup([
        [KeyboardButton("📕English"),KeyboardButton("📓Matematika")],
        [KeyboardButton("📚Dasturlash tillari")]],
        resize_keyboard=True
    )
    return keyboard
def English():
    keyboard=ReplyKeyboardMarkup([
        [KeyboardButton("📉Level")],
        [KeyboardButton("Determine your level!")]],
        resize_keyboard=True
    )
    return keyboard
def Level():
    keyboard=ReplyKeyboardMarkup([
        [KeyboardButton("A1"),KeyboardButton("A2")],
        [KeyboardButton("B1"),KeyboardButton("B2")],
        [KeyboardButton("C1"),KeyboardButton("C2")],
        [KeyboardButton("orqaga")]
        ],
        resize_keyboard=True
    )
    return keyboard
def home_keyboard():
    keyboard = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("🗃️Topshiriqlar"),
                KeyboardButton("📈Statistika")
            ],
        ],
        resize_keyboard=True
    )
    return keyboard

def tasks_keyboard(user_id):
    tasks=db.get_all_tasks(user_id)
    buttons=[]
    for i in tasks:
        text = "🕔  "+i["title"]
        if i["completed"]:
            text = "✅  "+i["title"]
        buttons.append([InlineKeyboardButton(text=text, callback_data=f"task_id:{i.doc_id}")])
    return InlineKeyboardMarkup(buttons)

def task_keyboard(task_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="❌ bekor qilish",callback_data=f"remove:{task_id}"),
                InlineKeyboardButton(text="✅ bajarildi",callback_data=f"done:{task_id}")
            ]
        ]
    )
