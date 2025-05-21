# Импортируем необходимые классы.
# @museum_by_coding_lover_bot --> ник в тг
import logging
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
BOT_TOKEN = '7407495360:AAFZEskbiSlbEPlIgcDzqXnHXUipIWKXZaE'


async def start(update, context):
    photo_path = '1.jpg'  # например, фото зала 1
    await update.message.reply_photo(photo=open(photo_path, 'rb'), caption='''🏛 Вход:
Добро пожаловать в музей!
Пожалуйста, сдайте верхнюю одежду в гардероб. 🧥
/enter - выход
<адрес> - куда хотим пойти
Это может быть:
зал 1
зал 2
зал 3
зал 4
выход
''')
    return 1


async def first(update, context):
    await update.message.reply_text('''🖼 Зал 1 — Введение в искусство:
В данном зале представлено общее введение в искусство разных эпох.

➡️ Вы можете пройти в:
• Зал 2 — Средневековье, иконы и витражи
• Выход — Завершить экскурсию и покинуть музей''')
    return 1


async def second(update, context):
    await update.message.reply_text('''🏰 Зал 2 — Средневековье:
В данном зале представлено искусство Средневековья: иконы, фрески, витражи и рыцарское вооружение.

➡️ Вы можете пройти в:
• Зал 3 — Ренессанс: эпоха возрождения гения''')
    return 2


async def third(update, context):
    await update.message.reply_text('''🎨 Зал 3 — Ренессанс:
В данном зале представлены шедевры Ренессанса: живопись Леонардо да Винчи, 
Микеланджело, Рафаэля.

➡️ Вы можете пройти в:
• Зал 1 — Вернуться к истокам искусства'
• Зал 4 — Современное искусство, новые формы и смыслы''')
    return 3


async def fourth(update, context):
    await update.message.reply_text('''🧠 Зал 4 — Современное искусство:
В данном зале представлено современное искусство: цифровые инсталляции, перформансы, концептуальные работы.

➡️ Вы можете пройти в:
• Зал 1 — Вернуться к истокам искусства''')
    return 4


async def exit(update, context):
    await update.message.reply_text('''🚪 Выход:
Всего доброго!
Не забудьте забрать верхнюю одежду в гардеробе. 🧥''')
    return ConversationHandler.END


async def route(update, context):
    s = update.message.text.lower()
    if s == 'зал 1':
        await first(update, context)
    elif s == 'зал 2':
        await second(update, context)
    elif s == 'зал 3':
        await third(update, context)
    elif s == 'зал 4':
        await fourth(update, context)
    elif s == 'выход':
        await exit(update, context)
    else:
        update.message.reply_text('''Некорректный ввод''')


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, route)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, route)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, route)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, route)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('exit', exit)]
    )

    application.add_handler(conv_handler)

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()


