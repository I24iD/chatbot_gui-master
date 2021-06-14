#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from chatbot import Chatbot


def main():
    # Listen
    zufallsantworten = ["Oh wirklich...",
                        "Interessant",
                        "Das kann man so sehen",
                        "Ich verstehe"]
    reaktionen = {"hallo": "aber hallo",
                  "geht": "was verstehst du darunter?",
                  "schmeckt": "Ich habe keinen Geschmackssinn."}

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
