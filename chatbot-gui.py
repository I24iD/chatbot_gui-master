#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
        QMessageBox, QLabel, QLineEdit, QGridLayout, QPushButton)
from chatbot import Chatbot


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        # Add grid layout
        self.chatbot_label = QLabel('Willkommen! Worüber wollen Sie sprechen?')
        self.input_label = QLabel('Ihre Frage oder Antwort:')
        self.chatbot_input = QLineEdit()
        self.chatbot_input.returnPressed.connect(self.button_clicked)

        button = QPushButton('Los!', self)
        button.clicked.connect(self.button_clicked)
        button.setAutoDefault(True)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.chatbot_label, 1, 0, 1, 3)
        grid.addWidget(self.input_label, 2, 0, 1, 3)
        grid.addWidget(self.chatbot_input, 3, 0, 1, 3)

        grid.addWidget(button, 3, 3)

        widget.setLayout(grid)

        self.title = 'Einfacher Chatbot'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 200

        self.init_ui()

    def button_clicked(self):
        # Listen
        zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]
        reaktionen = {"hallo": "aber hallo",
                    "geht": "Was verstehst Du darunter",
                    "schmeckt": "Ich habe keinen Geschmackssinn"}

        if self.chatbot_input.text() == "":
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText('Keine Eingabe!')
            message.setInformativeText('Ohne Frage kann ich nicht antworten.')
            message.exec_()
        else:
            bot = Chatbot(reaktionen, zufallsantworten)
            bot.set_Message(self.chatbot_input.text())
            self.chatbot_label.setText(bot.get_Response())
            self.chatbot_input.setText("")

    def init_ui(self):
        # Set basic window layout
        self.setWindowTitle(self.title)
        # self.setWindowIcon(QIcon(self.window_icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
