"""
This module contains the main code to execute the quiz.
"""
import pyfiglet, colorama, os, operator
from Questions import *
from userclass import *
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt
import pandas as pd

def main_quiz():
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    Function for the starting of the quiz. This function will call other functions as required.
    """
    quiz_header()
    quiz_table()
    menu_choice()

def quiz_header():
    """
    (1) Feature - This header being created through use of an external library imported and utilized correctly to display the 'header' for the quiz.
    This utilizes ASCII art.
    """
    result = pyfiglet.figlet_format("Quiz",font= 'sub-zero')
    console.print((result),justify="center")

def quiz_table():
    """
    (2) Feature - This is the generation of a table to display the main menu for the quiz.
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
    (3) Feature - This function is for the main menu logic tree. Depending on the user choice a further function will be called accordingly.
    """
    try:
        while True:
            choice = IntPrompt.ask("[green] Please input your choice ")
            if (choice == 1):
                choice_one()
            elif choice == 2:
                choice_two()
            elif (choice == 3):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have chosen to exit the game!")
                break
                '(Choice Three) When invoked this function will exit the game.'
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                quiz_header()
                quiz_table()
                console.print(":cross_mark:","[red] INVALID OPTION",":cross_mark:","\n:cross_mark:","[red] PLEASE TRY AGAIN",":cross_mark:" ,style="bold")
                
    except KeyboardInterrupt:
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exit()
                except SystemExit:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exit()

def choice_one():
    '(Choice One) This function when invoked will clear the previous screen and then the player will navigate to the main menu of the game and perform a function call on question_quiz_warcraft()'
    os.system('cls' if os.name == 'nt' else 'clear')
    question_quiz_warcraft()

def choice_two():
    '(Choice Two) This function when invoked will clear the previous screen and then the player will navigate to the View the highscores and the function call will load the scoredboard from csv.'
    os.system('cls' if os.name == 'nt' else 'clear')
    view_highscores()
    try:
        choice = IntPrompt.ask("[green]If you would like to try again press 1 otherwise press 2 to exit: ")
        if (choice == 1):
            main_quiz()
        elif (choice == 2):
            exit()
    except ValueError:
        print("Invalid option - Please try again.")

def view_highscores():
        csvData = pd.read_csv("highscores.csv",index_col=False)
        csvData.sort_values(["Score"],axis=0,ascending=[False],inplace=True)
        csvData.to_csv("highscores.csv",index=False)
        csvScore = pd.read_csv("highscores.csv",usecols=["Score"])
        csvFirstName = pd.read_csv("highscores.csv",usecols=["First Name"])
        csvLastName = pd.read_csv("highscores.csv",usecols=["Last Name"])
        csvLines = int(csvData.shape[1])
        # Creating the scoreboard with Rich library.
        score_table = Table(title="Score Board")
        score_table.add_column("First Name")
        score_table.add_column("Last Name")
        score_table.add_column("Score")
        score_table.add_row(csvFirstName.to_string(index=False,header=None),csvLastName.to_string(index=False,header=None),csvScore.to_string(index=False,header=None))
        console.print(score_table, justify="center")

main_quiz()
'Here I am invoking the main_quiz function to start the quiz.'



# 'Here I sort the csv rows by the column score'
# 