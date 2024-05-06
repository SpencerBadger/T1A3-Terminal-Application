from colorama import Fore
import pyfiglet
import csv
from rich.console import Console
from rich.table import Table
from Questions import question_quiz

# def scores():
#     try:
#         quiz_questions = []
#         scores = 'scores.json'
#         with open(scores) as f:
#             json.dump(quiz_questions, f)
#     except:
#         print("This didn't work")

def quiz_header():
    from pyfiglet import figlet_format
    from colorama import Fore

    result = pyfiglet.figlet_format("Quiz",font= 'slant', justify="center")
    return (print(result))

def main_quiz():
    try:
        quiz_header()
        table = Table()
        table.add_column("Option (1)", justify="center")
        table.add_column("Option (2)", justify="center")
        table.add_column("Option (3)", justify="center")
        table.add_row(" Play Quiz","View Highscores"," Exit Game")
        console = Console()
        console.print(table)

        choice = int(input("Please input your choice: "))
        if choice == 1:
            print("You have chosen to play the quiz!")
            question_quiz()
            
           
        elif choice == 2:
            print("You have chosen to view highscores!")
            # def view_highscores():
            #         try:
            #             with open('scores.csv') as r:
            #                 for line in r:
            #                     print(line)
            #         except:
            #             print("This didn't work")
            # view_highscores()
            main_quiz()

        elif choice == 3:
            print("You have chosen to exit the game!")
            exit()
        else:
            main_quiz()
    except ValueError:
        console.print("\n You have entered an invalid choice! \n", justify="center")
        console.print(":cross_mark:" + "[red] Please Enter a valid choice." + ":cross_mark: \n ", justify="center")
        return(main_quiz())

