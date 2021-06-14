#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random


class Chatbot:
    """ Eine Klasse für einen Chatbot
        Verwendung:
        bot = Chatbot(reaktionen, zufallsantworten)
    """

    def __init__(self, reaktionen, zufallsantworten):
        # Konstruktor der Klassse
        self.__reaktionen = dict(reaktionen)
        self.__zufallsantworten = list(zufallsantworten)

    def set_Message(self, message):
        """ set_Message
            wird verwendet, um dem Chatbot die Eingabe des Benutzers zu übergeben
            Verwendung:
            bot.set_Message(nutzereingabe)
        """
        self.__message = str(message)

    def get_Response(self):
        """ get_Response
            wird verwendet, um den Chatbot die richtige Antwort zu entlocken
            Verwendung:
            response = bot.get_Response()
        """
        self.__message = self.__message.lower()
        self.__words = self.__message.split()
        self.__intelligentAnswers = False

        for word in self.__words:
            if word in self.__reaktionen:
                self.__intelligentAnswers = True
                self.__response = self.__reaktionen[word]
        if not self.__intelligentAnswers:
            self.__response = random.choice(self.__zufallsantworten)

        return self.__response


def main():
    # Listen
    zufallsantworten = ["Entschuldigung,das habe ich nicht verstanden!",
                        "Interessant",
                        "Ach wirklich...",
                        "Ich verstehe!"]
    reaktionen = {"hallo": "Schönen guten Tag!",
                  "geht": "Mir geht es gut! Und wie geht es Ihnen?",
                  "gefühle": "Das weiß ich nicht,denn ich habe keine Gefühle!"}

    # Ausgabe Begrüßung
    print("Willkommen beim Chatbot (V3)")
    print("Worüber möchten Sie sprechen?")
    print("Zum beenden geben Sie bye ein...")
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
    print("Peace!Bis zum nächsten Mal.")


if __name__ == "__main__":
    main()
