# chatbot_new/chatbot_gui-master

### Beschreibung
Ein Chatbot mit verschiedenen Oberflächen. Beispiel für objektortientierte Programmierung und die Verwendung von Frameworks.

Zusätzlich: Verwendung von Docker und CI/CD für Test und Verteilung.

### Versionen
1. v2: einfacher Chatbot mit vorgegebenen Fragen und Antworten
2. v3: Chatbot mit künstlicher Intelligenz

### Installation
´´´bash
1. git clone https://github.com/I24iD/chatbot_new
2. cd chatbot_new
3. mkdir v3/model
´´´

### Benutzung
1. v2:
	´´´python
	from chatbot import Chatbot
	bot = Chatbot(reaktionen, zufallsantworten)
	bot.set_Message(eingabe)
	ausgabe = bot.get_Response()
	´´´
	##### Hilfe mit python help chatbot

2. v3:	
	´´´python
	from chatbot_ai import chatbot_ai
	bot = chatbot_ai(jsonfile)
	bot.set_Message(eingabe)
	ausgabe = bot.get_Response()
	´´´
