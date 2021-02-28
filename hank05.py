from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Hank')

bot = ChatBot(
    'Hank',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)
conversa.train([
    'oi?',
    'Eae',
    'Qual o seu nome?',
    'Hank, o seu Amigão',
    'Obrigado por existir para mim amigo',
    'Igualmente meu parceiro',
    'vamos conversar',
    'Estou farto de improfícuas agonias',
    'Mas tu mesmo, não disseste que tudo é ilusão, sonhar é sabê-lo?',
    'E quem disse que mostro?',
    'À arte o mundo cria',
    'E o nome inútil que teu corpo usou, vivo, na terra, como uma alma não lembra'
    ])

while True:
    try:
        resposta = bot.get_response(input("Eu: "))
        if float(resposta.confidence) > 0.5:
            print("Hank: ", resposta)
        else:
            print("Eu não entendi :(")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break