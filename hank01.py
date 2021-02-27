from chatterbot import ChatBot


# Uncomment the following lines to enable verbose logging (Remova o comentário das linhas a seguir para habilitar o registro detalhado)
import logging
logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot(Crie uma nova instância de um ChatBot)
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

print('Hello, world! Olá Mundo! Vamos começar a conversar...')

# The following loop will execute each time the user enters input (O loop seguinte será executado cada vez que o usuário inserir uma entrada)
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break