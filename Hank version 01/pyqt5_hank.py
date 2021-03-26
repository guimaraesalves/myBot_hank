from PyQt5 import QtCore, QtGui, QtWidgets
from nltk.chat.util import Chat, reflections


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
            "Olá, seja bem-vindo, pergunte qualquer coisa. Digite 'quit' em letras minúsculas para sair"
        )

        pairs = [
            [r"Olá! eu sou o (.*)", ["Olá %1 , Como você está?",]],
            [
                r"(Qual é o seu nome?|Quem é você?)",
                ["Eu sou o Hank.\n Seu Amigão."],
            ],
            [
                r"(Qual é a sua localização (Localização|cidade)?|de onde você está falando)",
                [
                    "Eu estou aqui, no seu computador\n dentro da sua cabeça"
                ],
            ],
            [
                r"(you) are (.*)",
                ["i am very very intelligent computer  \n %1 not %2 may be you are %2"],
            ],
            [
                r"is human (.*)",
                [" i think human is not very intelligent but may be %1"],
            ],
            [r"(.*)", ["what!\n Sorry,i can't understand "]],
        ]

        self._chat = Chat(pairs, reflections)

    @property
    def chat(self):
        return self._chat

    @QtCore.pyqtSlot()
    def on_return_pressed(self):
        text = self.input_le.text()
        if text:
            res = self.chat.respond(text)
            self.output_te.append("[Eu]: {}".format(text))
            self.output_te.append("[Hank]: {}".format(res))
            self.input_le.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
