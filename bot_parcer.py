import telebot

api_token_path = 'E:\\обучение\\'
file_name = 'tokens_for_bots.txt'


def get_token(token_path, name):
    api_file = open((token_path + name), "r")
    data = api_file.read().split('\n')
    api_token = data[1].split(': ')[1]  # return 1) second string 2)split between :_ 3)find second element into result list
    api_file.close()
    return api_token    # return API token from txt file


# def settings_bot():
client = telebot.TeleBot(get_token(api_token_path, file_name))


@client.message_handler(content_types=['text'])


def get_text(message):
    if message.text.lower() == "hi":
        client.send_message(message.chat.id, 'hello friend')


client.polling(none_stop=True, interval=0)
