import telegram

import openai

openai.api_key = "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"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am ChatGPT, your personal AI assistant. How can I assist you today?")

def reply(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

def main():
    updater = Updater(token="6141554097:AAFq2sznljgTssX9ul5DbE7bxDkNVKnF500", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    reply_handler = MessageHandler(Filters.text & ~Filters.command, reply)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(reply_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
