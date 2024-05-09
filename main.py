"""
This module contains the main code to execute the quiz.
"""
import pyfiglet
import os
from Questions import *
from userclass import *
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt
import pandas as pd

def main_quiz():
    """
    main_quiz() Starts the quiz game.
    """
    clear_screen()
    quiz_header()
    quiz_table()
    menu_choice()

def quiz_header():
    """
    (1) Feature - quiz_header() Displays the Quiz Header when called. Utilizing ASCII art.
    """
    result = pyfiglet.figlet_format("Quiz",font= 'sub-zero')
    console.print((result),justify="center")

def quiz_table():
    """
    (2) Feature - quiz_table() Generates and displays the main menu for the quiz.
    """
    table = Table()
    table.add_column("Option (1)", justify="center")
    table.add_column("Option (2)", justify="center")
    table.add_column("Option (3)", justify="center")
    table.add_row(" Play Quiz","View Highscores"," Exit Game")
    console = Console()
    console.print(table, justify="center")

def menu_choice():
    """
    (3) Feature - menu_choice() Handles the main menu logic tree.
    """
    try:
        while True:
            choice = IntPrompt.ask("[green] Please input your choice ")
            if (choice == 1):
                """
                Calls the choice_one function.
                """
                choice_one()
            elif choice == 2:
                """
                Calls the choice_two function.
                """
                choice_two()
            elif (choice == 3):
                clear_screen()
                print("You have chosen to exit the game!")
                exit()
                """
                (Choice Three) If invoked this function will exit the game.
                """
            else:
                clear_screen()
                quiz_header()
                quiz_table()
                console.print(":cross_mark:","[red] INVALID OPTION",":cross_mark:","\n:cross_mark:","[red] PLEASE TRY AGAIN",":cross_mark:" ,style="bold")
                
    except KeyboardInterrupt:
                try:
                    clear_screen()
                    exit()
                except SystemExit:
                    clear_screen()
                    exit()

def choice_one():
    """
    (Choice One) choice_one() When invoked will clear the current screen and call the question_quiz_warcraft() function.
    """
    clear_screen()
    question_quiz_warcraft()

def choice_two():
    """
    (Choice Two) choice_two() when will clear the current screen and then the call the view_highscores() function, this will display the scoreboard by invoking the view_highscores() function.
    """
    clear_screen()
    view_highscores()
    

def view_highscores():
        csv_data = pd.read_csv("highscores.csv",index_col=False)
        csv_data.sort_values(["Score"],axis=0,ascending=[False],inplace=True)
        csv_data.to_csv("highscores.csv",index=False)
        csv_score = pd.read_csv("highscores.csv",usecols=["Score"])
        csv_first_name = pd.read_csv("highscores.csv",usecols=["First Name"])
        csv_last_name = pd.read_csv("highscores.csv",usecols=["Last Name"])
        csv_lines = int(csv_data.shape[1])
        # Creating the scoreboard with Rich library.
        score_table = Table(title="Score Board")
        score_table.add_column("First Name", style="cyan")
        score_table.add_column("Last Name")
        score_table.add_column("Score",style="green")
        score_table.add_row(csv_first_name.to_string(index=False,header=None),csv_last_name.to_string(index=False,header=None),csv_score.to_string(index=False,header=None))
        console.print(score_table, justify="center")
        try:
            choice = IntPrompt.ask("[green]If you would like to try again press 1 otherwise press 2 to exit: ")
            if (choice == 1):
                main_quiz()
            elif (choice == 2):
                exit()
        except ValueError:
            print("Invalid option - Please try again.")
        except KeyboardInterrupt:
                    clear_screen()
                    exit()

                
main_quiz()
"""
main_quiz function call to start the game.
"""
