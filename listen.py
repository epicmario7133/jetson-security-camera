from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
with open('data.json') as json_file: #Load Token
    data = json.load(json_file)
TOKEN = data["api_key"]


def on(update, context):
    update.message.reply_text('AI has been enabled')
    data["on"] = "1"
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def off(update, context):
    update.message.reply_text('AI has been disabled')
    data["on"] = "0"
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("on", on))
    dispatcher.add_handler(CommandHandler("off", off))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
