from slackbot.bot import Bot
from slackbot.bot import listen_to

balance = 0

@listen_to('set (.*)')
def set_balance(message, money):
    try:
        money = int(money)
        global balance
        balance = money
        message.send('set balance:{}'.format(balance))
    except:
        message.send('please num')


@listen_to('add (.*)')
def add_balance(message, money):
    try:
        money = int(money)
        global balance
        str1 = 'old_balance:' + balance + '\n'
        balance += money
        str2 = 'Add:' + money + '\n'
        str3 = 'new_balance' + balance + '\n'
        message.send(str1+str2+str3)
    except:
        message.send('please num')

@listen_to('cost (.*)')
def cost_balance(message, money):
    try:
        money = int(money)
        global balance
        str1 = 'old_balance:' + balance + '\n'
        balance -= money
        str2 = 'Cost:' + money + '\n'
        str3 = 'new_balance' + balance + '\n'
        message.send(str1+str2+str3)
    except:
        message.send('please num')

@listen_to('balance')
def send_balance(message):
    message.send(balance)

bot = Bot()
bot.run()
