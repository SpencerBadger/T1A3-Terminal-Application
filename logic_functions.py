import pyfiglet, colorama, os, json
from rich.console import Console
from rich.table import Table
from Questions import *

def main_quiz():
    quiz_header()
    quiz_table()
    menu_choice()

def quiz_header():
    result = pyfiglet.figlet_format("Quiz",font= 'slant', justify="center")
    return (print(result))

def quiz_table():
    table = Table()
    table.add_column("Option (1)", justify="center")
    table.add_column("Option (2)", justify="center")
    table.add_column("Option (3)", justify="center")
    table.add_row(" Play Quiz","View Highscores"," Exit Game")
    console = Console()
    console.print(table)

def menu_choice():
    choice = int(input("Please input your choice: "))
    if choice == 1:
        choice_one()
    elif choice == 2:
        choice_two()
    elif choice == 3:
        choice_three()

def choice_one():
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print("Please select which quiz you would like to play:")
        # print("(1) Warcraft ", "(2) Fallout ","(3) Emptiness")
        # quiz_selection = int(input("Which quiz would you like to play?"))
        # if quiz_selection == 1:
            question_quiz_warcraft()
        # elif quiz_selection == 2:
        #     print("Option 2")
        # elif quiz_selection == 3:
        #     print("Option 3")


def choice_two():
     os.system('cls' if os.name == 'nt' else 'clear')
     print("You have chosen to view highscores!")
     load_data()
     escape = input("Would you like to exit the program? (y/n)")

def choice_three():
    print("You have chosen to exit the game!")
    exit()



