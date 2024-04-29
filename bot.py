from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
import handlers

def main() -> None:

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"^🗃️Topshiriqlar$"), handlers.send_task))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handlers.compile_cpp))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
