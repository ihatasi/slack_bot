from slackbot.bot import Bot\

@respond_to('what?')
def what(message):
    message.reply('free')
@respond_to('say (.*)')
def say(message, word):
    message.reply(word + '!')
@respond_to('join (.*) (.*)')
def say(message, word1, word2):
    message.reply(word1 + '&' + word2 + '!')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
