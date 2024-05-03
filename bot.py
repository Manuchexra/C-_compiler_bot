from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
import handlers

def main() -> None:

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"📚Dasturlash tillari"), handlers.dasturlash_tillari))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"📕English"), handlers.English))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"📉Level"),handlers.Level))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"Determine your level!"),handlers.get_level))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"orqaga"),handlers.English))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"^🗃️Topshiriqlar$"), handlers.send_task))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handlers.compile_cpp))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
