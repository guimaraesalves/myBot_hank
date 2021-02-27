from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Hank')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hello, World!!",
    "Seja bem vindo meu amigo Hank!!!",
    "Olá, Mundo! Qual é o seu nome meu amigo humano?",
    "Eu sou o Mateus."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')

print(response)
