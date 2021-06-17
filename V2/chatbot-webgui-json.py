#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash
from chatbot import Chatbot
import json

json = json.loads(open('antworten.json').read())
antworten = json['antworten']
reaktion = json['reaktionen']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pa$$w0rd'


@app.route('/', methods=('GET', 'POST'))
def index():
    chatbot_label = "Hallo, worüber wollen Sie sprechen?"

    # Listen
    zufallsantworten = antworten
    reaktionen = reaktion

    # Logik
    if request.method == 'POST':
        chatbot_input = request.form['chatbot_input']
        if not chatbot_input:
            flash("Ohne Frage kann ich nicht antworten!")
        else:
            bot = Chatbot(reaktionen, zufallsantworten)
            bot.set_Message(chatbot_input)
            chatbot_label = bot.get_Response()

    return render_template('chatbot.html', chatbot_label=chatbot_label)
