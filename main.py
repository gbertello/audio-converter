#!/usr/bin/env python3

from app.app import App


ORIGIN_PATH = "/Users/gbertello/Desktop/Musique de Pierre/"
DESTINATION_PATH = "/Users/gbertello/Desktop/Musique de Pierre (converted)/"
RULES_PATH = "/Users/gbertello/Programmes/audio-converter/rules.json"
App(ORIGIN_PATH, DESTINATION_PATH, RULES_PATH).main()
