import telegram
bot = telegram.Bot(token='8435778620:AAF_7nwwpLrMiZdMXYicuxxXiHGLi-PfoWc')
print(bot.get_me())
bot.send_message(chat_id='@spaceteee', text='какой-нибудь текст')