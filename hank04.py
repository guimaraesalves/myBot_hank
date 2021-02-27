from chatterbot import ChatBot


bot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

# Print an example of getting one math based response (Imprima um exemplo de como obter uma resposta baseada em matemática)
response = bot.get_response('Quanto é 5 * 9?')
print(response)

# Print an example of getting one time based response (Imprima um exemplo de como obter uma resposta baseada em tempo)
response = bot.get_response('Que horas são?')
print(response)