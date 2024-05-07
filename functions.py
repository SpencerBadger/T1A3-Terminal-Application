# from game import Game_Logic, Score_Board


# def game_start():
#     choice = int(input("Please input your choice:"))
#     Game_Logic.menu(choice)

# score = 10

import json

def load_data():
    data = {}
    with open("scoreboard.json","r") as f:
        data = json.load(f)
        print(data)

load_data()
# game_start()
# user_record(score)
