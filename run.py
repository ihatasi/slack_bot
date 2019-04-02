from slackbot.bot import Bot
from slackbot.bot import respond_to

@respond_to('what?')
def what(message):
    message.reply('free')

@respond_to('say (.*)')
def say(message, word):
    message.reply(word + '!')


bot = Bot()
bot.run()
