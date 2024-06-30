import json
import pprint

import requests
from datetime import datetime

headers = {"x-fsign": "SW9D1eZo"}
list_of_matches = []


class Game:
    date: datetime
    first_command: str
    second_command: str
    score: str

    def __init__(self, date, first_command, second_command, score):
        self.date = date
        self.first_command = first_command
        self.second_command = second_command
        self.score = score
    # f_1_-1_7_ru-kz_1


def parser_all_matches_flashscore(feed, sec_feed):
    url = f'https://local-ruua.flashscore.ninja/46/x/feed/{feed}'
    response = requests.get(url=url, headers=headers)
    data = response.text.split('¬')
    arr = get_koef(sec_feed)
    main_str = ''
    data_list = [{}]

    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]

        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})

    for game in data_list:
        if 'AA' in list(game.keys())[0]:
            # date = datetime.fromtimestamp(int(game.get("AD")))
            XA = ''
            XB = ''
            XC = ''

            code = game.get("~AA")
            for i in arr:
                text = i.split('/')
                if text[0] == code:
                    XA = text[1]
                    XB = text[2]
                    XC = text[3]
            date = datetime.fromtimestamp(int(game.get("AD")))
            team_1 = game.get("AE")
            team_2 = game.get("AF")
            score = f'{game.get("AG")} : {game.get("AH")}'

            main_str += f'{date}/{team_1}/{team_2}/{score}/{XA}/{XB}/{XC}*'

            # match = Game(date=date, first_command=team_1, second_command=team_2, score=score)

    return main_str


def get_koef(feed):
    url = f'https://local-ruua.flashscore.ninja/46/x/feed/{feed}'
    response = requests.get(url=url, headers=headers)
    data = response.text.split('¬')
    arr = []
    data_list = [{}]

    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]

        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})

    for game in data_list:
        if 'AA' in list(game.keys())[0]:
            code = game.get("~AA")
            XA = game.get("XA")
            XB = game.get("XB")
            XC = game.get("XC")

            arr.append(f'{code}/{XA}/{XB}/{XC}')
    return arr

# get_koef('fo_1_0_7_ru-kz_1_0')
# f_1_-1_7_ru-kz_1
# 'fo_1_0_7_ru-kz_1_0'
