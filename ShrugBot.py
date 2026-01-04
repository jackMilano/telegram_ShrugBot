from sys import argv
from time import sleep
import telepot              # Python framework for Telegram Bot API
from random import randint

# ¯\_(ツ)_/¯


def handle(msg):
    flavor = telepot.flavor(msg)

    # chat message
    if flavor == 'chat':
        content_type, chat_type, chat_id = telepot.glance(msg)

        if chat_type == 'group' or chat_type == 'private':
            if content_type == 'text':
                text = msg['text']
                print('text = ' + text)
                if randint(1, 20) == 1:
                    bot.sendMessage(chat_id, r'¯\_(ツ)_/¯')
            else:
                print('content_type = ' + content_type)
        else:
            print('chat_type = ' + chat_type)

    # callback query - originated from a callback button
    elif flavor == 'callback_query':
        query_id, from_id, query_data = telepot.glance(msg, flavor=flavor)
        print('Callback query:', query_id, from_id, query_data)

    # inline query - need `/setinline`
    elif flavor == 'inline_query':
        query_id, from_id, query_string = telepot.glance(msg, flavor=flavor)
        print('Inline Query:', query_id, from_id, query_string)

        # Compose your own answers
        articles = [{'type': 'article',
                     'id': 'abc',
                     'title': 'ABC',
                     'message_text': 'maaaaaan!'}]

        bot.answerInlineQuery(query_id, articles)

    # chosen inline result - need `/setinlinefeedback`
    elif flavor == 'chosen_inline_result':
        result_id, from_id, query_string = telepot.glance(msg, flavor=flavor)
        print('Chosen Inline Result:', result_id, from_id, query_string)
        # Remember the chosen answer to do better next time

    else:
        raise telepot.BadFlavor(msg)


# Token passed via command line to keep it secret.
TOKEN = argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

# Keep the program running.
while 1:
    sleep(10)
