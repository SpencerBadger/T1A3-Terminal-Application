"""
This module contains the main code to execute the quiz.
"""
import pyfiglet
import os
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt
from Questions import *
from userclass import UserClass

def main_quiz():
    """
    Starts the quiz game.

    Parameters
    ----------
    None
        
    Returns
    ----------
    None

    """
    clear_screen()
    quiz_header()
    quiz_table()
    menu_choice()

def quiz_header():
    """
    Displays the Quiz Header when called. 
    Utilizing ASCII art.

    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    result = pyfiglet.figlet_format("Quiz",font= 'sub-zero')
    console.print((result),justify="center")

def quiz_table():
    """
    Generates and displays the main menu for the quiz.

    Parameters
    ----------
    None
        
    Returns
    ----------
    None
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
    Feature 
    ----------
    Handles the main menu logic tree.

    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    try:
        while True:
            choice = IntPrompt.ask("[green] Please input your choice ")
            if choice == 1:
                choice_one()
            elif choice == 2:
                choice_two()
            elif choice == 3:
                clear_screen()
                print("You have chosen to exit the game!")
                exit()
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

    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    clear_screen()
    question_quiz_warcraft()

def choice_two():
    """
    (Choice Two) choice_two() when will clear the current screen and then the call the view_highscores() function, this will display the scoreboard by invoking the view_highscores() function.

    Parameters
    ----------
    None
        
    Returns
    ----------
    None  
    """
    clear_screen()
    view_highscores()
    

def view_highscores():
    """
    Sorts the data by score and then displays the scoreboard populated with first, last name and score.
    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """     
    csv_data = pd.read_csv("highscores.csv",index_col=False)
    csv_data.sort_values(["Score"],axis=0,ascending=[False],inplace=True)
    csv_data.to_csv("highscores.csv",index=False)
    csv_score = pd.read_csv("highscores.csv",usecols=["Score"])
    csv_first_name = pd.read_csv("highscores.csv",usecols=["First Name"])
    csv_last_name = pd.read_csv("highscores.csv",usecols=["Last Name"])
    csv_lines = int(csv_data.shape[1])
    score_table = Table(title="Score Board")
    score_table.add_column("First Name", style="cyan")
    score_table.add_column("Last Name")
    score_table.add_column("Score",style="green")
    score_table.add_row(csv_first_name.to_string(index=False,header=None),csv_last_name.to_string(index=False,header=None),csv_score.to_string(index=False,header=None))
    console.print(score_table, justify="center")
    scoreboard_exit()
        
def scoreboard_exit():
    """
    User Input for exiting or returning to main menu.
    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """ 
    try:
        user_score_choice = IntPrompt.ask("[green]Press 1: Main Menu, Press 2: Exit")
        if (user_score_choice == 1):
            main_quiz()
        elif (user_score_choice == 2):
            exit()
        else:
            clear_screen()
            (console.print(":cross_mark:", "[red] INVALID OPTION", ":cross_mark:", "\n:cross_mark:", "[red]Press 1: Main Menu, Press 2: Exit", ":cross_mark:", style="bold", justify="center"))
            raise AttributeError(scoreboard_exit())
    except ValueError:
            clear_screen()
            (console.print(":cross_mark:", "[red] INVALID OPTION", ":cross_mark:", "\n:cross_mark:", "[red] PLEASE TRY A 1 OR A 2", ":cross_mark:", style="bold", justify="center"))
            scoreboard_exit()

if __name__ == "__main__":
    main_quiz()
