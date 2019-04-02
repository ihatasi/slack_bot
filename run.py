from slackbot.bot import Bot
from slackbot.bot import listen_to

money = 0

@listen_to('set (.*)')
def what(message, set_money):
    try:
        set_money = int(set_money)
        global money
        money = set_money
        message.reply('set money:', money)
    except:
        message.reply('please num')


@listen_to('say (.*)')
def say(message, word):
    message.reply(word + '!')


bot = Bot()
bot.run()
