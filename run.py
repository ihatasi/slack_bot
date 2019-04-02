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
        str1 = 'old balance:' + str(balance) + '\n'
        balance += money
        str2 = 'Add:' + str(money) + '\n'
        str3 = 'new balance:' + str(balance) + '\n'
        message.send(str1+str2+str3)
    except:
        message.send('please num')

@listen_to('cost (.*) (.*)')
def cost_balance(message, money, obj):
    if obj == None:
        message.send('Set obj at now!!!!')
    else:
        try:
            money = int(money)
            global balance
            str1 = 'old balance:' + str(balance) + '\n'
            balance -= money
            str2 = 'Cost:' + str(money) + '\n'
            str3 = 'new balance:' + str(balance) + '\n'
            str4 = 'for ' + str(obj) + '\n'
            message.send(str1+str2+str3+str4)
        except:
            message.send('please num')

@listen_to('balance')
def send_balance(message):
    global balance
    str1 = 'now balance:' + str(balance)
    message.send(str1)

bot = Bot()
bot.run()
