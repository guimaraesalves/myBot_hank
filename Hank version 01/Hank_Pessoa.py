from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from PyQt5 import QtCore, QtGui, QtWidgets
#from nltk.chat.util import Chat, reflections

bot = ChatBot("Pessoa Hank")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        

        self.output_te = QtWidgets.QTextEdit(readOnly=True)
        self.input_le = QtWidgets.QLineEdit(returnPressed=self.on_return_pressed)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addWidget(self.output_te)
        lay.addWidget(self.input_le)

        self.output_te.setPlainText(
            "Olá, Navegar é preciso!"
        )

        pairs = [
            
            'Olá',
            'Tudo vale a pena quando a alma não é pequena.',
            'Eu sou o hank e você',
            'Tenho em mim todos os sonhos do mundo...',
            'Para Viajar basta existir...',
            'A arte é a autoexpressão lutando para ser absoluta.',
            'Não escrevo em português. Escrevo eu mesmo.',
            'Há tanta suavidade em nada dizer e tudo entender...',
            'Deus quer, o homem sonha, a obra nasce.',
            'Sinto-me nascido a cada momento...',
            'Para a eternidade do Mundo...',
            'Porque eu sou do Tamanho do que vejo...',
            'E não da minha altura...',
            'Não é por nada que olho: é que eu gosto de ver as pessoas sendo.',
            'O verdadeiro cadáver não é o corpo(...), mas aquilo que deixou de viver.',
            'Façamos da interrupção um caminho novo.',
            'No fim tudo dá certo, e se não deu certo é porque ainda não chegou ao fim.',
            'Liberdade é o espaço que a felicidade precisa.',
            'Show de Bola',
            'O otimista erra tanto quanto o pessimista, mas não sofre por antecipação.',
            'Mas a convivência é feita também de silêncio, e distância.',
            'A música é o silêncio em movimento.',
            'Viva Nossa Senhora da Penha!!!',
            'Força',
            'Coragem',
            'Fé',
            'Ser feliz sem motivo é a mais autêntica forma de felicidade.',
            'O mundo é grande e cabe nesta janela sobre o mar.',
            'A minha vontade é forte, porém minha disposição de obedecer-lhe é fraca.',
            'União',
            'Paz meu rapaz!',
            'Show de Bola',
            'Na casa do médico, todos estão doentes',
            'Casa de ferreiro espeto de pau',
            'Quem não tem cão, caça com gato',
            'angu quente se come pelas beiradas',
            'Cedo ou tarde a verdade vai aparecer',
            '… preciso ter paciência para vencer',
            'Quem espera sempre alcança',
            'Água mole em pedra dura tanto bate até que fura.',
            'Para bom entendedor, meia palavra basta',
            'De grão em grão a galinha enche o papo',
            'Deus ajuda quem cedo madruga',
            'Quem quer faz, quem não quer manda',
            'Mais vale um pássaro na mão que dois voando',
            'Uma andorinha só não faz verão',
            'gosto da sua sinceridade',
            'obrigado',
            'você é de mais',
            'tu trouxeste luz a minha vida',
            'você é tão inteligente',
            'gosto do seu comportamento',
            'você me faz melhor',
            'nosso amor é que te faz melhor',
            'você é show de bola',
            'você também',
        ]

        trainer = ListTrainer(bot) 
        trainer.train(pairs)       

        #self._chat = Chat(pairs)


    @property
    def chat(self):
        return self._chat

    @QtCore.pyqtSlot()
    def on_return_pressed(self):
        text = self.input_le.text()
        if text:
            res = bot.get_response(text)
            self.output_te.append("[Eu]: {}".format(text))
            self.output_te.append("[Hank]: {}".format(res))
            self.input_le.clear()

import sys
if __name__ == "__main__":
    

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    