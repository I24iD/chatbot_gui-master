#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json


class file_handling:
    def __init__(self, filepath):
        try:
            with open(filepath) as antworten:
                self.antworten = json.load(antworten)
        except FileNotFoundError:
            print("Datei nicht gefunden.")
        except AttributeError:
            print("Keine Daten vorhanden")

        self.reaktionen = self.antworten['reaktionen']
        self.zufallsantworten = self.antworten['zufallsantworten']
