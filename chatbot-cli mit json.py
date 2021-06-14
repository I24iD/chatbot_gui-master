#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from chatbot import Chatbot
import json

json = json.loads(open('antworten.json').read())
antworten = json['antworten']
reaktion = json['reaktionen']


def main():
    # Listen
    zufallsantworten = antworten
    reaktionen = reaktion

    # Ausgabe Begrüßung
    print("Willkommen beim Chatbot (v2)")
    print("Zum Beenden geben Sie bye ein...")
    print("Worüber wollen Sie sprechen?")
    print("")

    # Chatbot-Objekt
    bot = Chatbot(reaktionen, zufallsantworten)

    # Logik
    nutzereingabe = ""
    while nutzereingabe != "bye":
        nutzereingabe = ""
        while nutzereingabe == "":
            nutzereingabe = input("Ihre Frage oder Antwort: ")
        if nutzereingabe == "bye":
            break
        bot.set_Message(nutzereingabe)
        print(bot.get_Response())

    # Ausgabe Verabschiedung
    print("Bis zum nächsten Mal.")


main()
