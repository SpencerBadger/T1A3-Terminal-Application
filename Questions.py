"""
This module contains various data relating to the quiz questions/answers logic for the quiz.
"""
import os
from rich.console import Console
from userclass import UserClass
from rich.prompt import IntPrompt
from rich.table import Table

console = Console()
data_table = [[],[],[],[]]

def question_quiz_warcraft():
        """
        Function for the quesitons and loop of said questions.

        Parameters
        ----------
        None
            
        Returns
        ----------
        None
        """
        questions = (
                "1. What is the name of the human capital city in World of Warcraft?",
                "2. Which of these classes are available to blood elves in World of Warcraft?",
                "3. Which four-wing instance located in Tirisfal Glades is frequently farmed by players in World of Warcraft?",
                "4. Who built Karazhan in World of Warcraft?",
                "5. What is the draenei racial heal called in World of Warcraft?" 
        )

        multiple_choice = (
                ("1. Ironforge", "2. Elwynn City", "3. Stormwind City", "4. Silvermoon City", "5. Booty Bay"),
                ("1. Warrior", "2. Warlock", "3. Priest", "4. Hunter","5. Rogue","6. All of the above"),
                ("1. Scarlet Monastery", "2. Auchindoun", "3. The Stockade", "4. Shadowfang Keep","5. The Deadmines"),
                ("1. Archimonde","2. Prince Kael'thas Sunstrider", "3. Guardian Aegwynn", "4. Kel'thuzad","5. Arthas Menethil"),
                ("1. Blessing of Argus", "2. Gift of the Naaru", "3. Symbol of Hope", "4. Velen's Touch","5. Call of the Exodar")
        )
        
        answers = (3,6,1,3,2)
        long_answer =("C. Stormwind City","F. All of the above","A. Scarlet Monastery","C. Guardian Aegwynn","B. Gift of the Naaru")
        score = 0

        #Loops for questions
        for question_number, question in enumerate(questions):
            os.system('cls' if os.name == 'nt' else 'clear')
            print_question(question, multiple_choice[question_number])
            guesses = get_user_input()
            
            data_table[0].append(questions[question_number])
            data_table[1].append(long_answer[question_number])
            'Appending the data table for presenting the scores and saving the results'
            
            if guesses == answers[question_number]:
                score += 1
                print_correct_answer()
                data_table[2].append("Correct")
                data_table[3].append(score)
            else:
                print_incorrect_answer()
                data_table[2].append("Incorrect")
            
        print_results_table(score)
        handle_next_steps(score)

 

def clear_screen():
    """
    Function to clear the screen, it is called when required.
    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_question(question, choices):
    """
    Function prints the question and the multiple choices for the answer.
    Parameters
    ----------
    question : str
    choices : list
    Returns
    ----------
    None
    """
    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
    console.print("[green]" + question, justify="center")
    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")

    for answer in choices:
        console.print(answer, justify="center")

    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")

def get_user_input():
    """
    Function will retrieve the user input.
    Parameters
    ----------
    None
        
    Returns
    ----------
    UserInput
    """
    try:
        return IntPrompt.ask("[green] Please enter the corresponding number: ")
    except KeyboardInterrupt:
        exit()
    except Exception:
        console.print(":cross_mark:","[red] INVALID OPTION",":cross_mark:","\n:cross_mark:","[red] PLEASE TRY AGAIN",":cross_mark:" ,style="bold")
        clear_screen()
        return get_user_input()
    
def print_correct_answer():
    """
    Function if called will print a message for a correct answer.
    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    console.print(":white_check_mark:" + "[green] Correct!", justify="center")
    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")

def print_incorrect_answer():
    """
    Function if called will print a message for an incorrect answer.
    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    console.print(":cross_mark:" + "[red] Incorrect!", justify="center")
    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")

def print_results_table(score):
    """
    Prints the results table.
    Parameters
    ----------
    score: int
        
    Returns
    ----------
    None
    """
    clear_screen()
    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
    table = Table(title="Results", show_lines=True)
    table.add_column("Question", justify="left")
    table.add_column("Answer", justify="left")
    table.add_column("Correct/Incorrect", justify="left")
    table.add_column("Score", justify="left")
    
    for i in range(len(data_table[0])):
        if data_table[2][i] == "Correct":
            table.add_row(data_table[0][i], data_table[1][i], "[green] Correct", ":white_check_mark:")
        else:
            table.add_row(data_table[0][i], data_table[1][i], "[red] Incorrect", ":cross_mark:")
    
    table.add_row("Total Score: ", "", "", str(score))
    console.print(table, justify="center")

def handle_next_steps(score):
    """
    Handles the next steps after completing the quiz.
    Parameters
    ----------
    score: int
        
    Returns
    ----------
    None
    """
    console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
    while True:
        what_next = IntPrompt.ask("[green]Would you like to save your results?\nPress (1) to save\nPress (2) to skip saving\n")
        if what_next == 1:
            write_data(score)
            input("Press Enter to continue...")
            from main import menu_choice
            menu_choice()
        elif what_next == 2:
                player_restart()
        else:
            console.print(":cross_mark:", "[red] INVALID OPTION", ":cross_mark:", "\n:cross_mark:", "[red] PLEASE TRY AGAIN", ":cross_mark:", style="bold")

def write_data(score):
    """
    Function will take users input for the UserClass(first name, last name) and score to save.
    Parameters
    ----------
    score: int
        
    Returns
    ----------
    None
    """
    first_name = input("Please provide your first name: ")
    last_name = input("Please provide your last name: ")
    user_details = UserClass(first_name, last_name, score)
    user_details.show()
    user_details.save_highscores()

def player_restart():
    """
    Function for user to exit the game or start again after finishing the quiz and not saving their score.
    Parameters
    ----------
    None
        
    Returns
    ----------
    None
    """
    while True:
        try:
            clear_screen()
            player_restart_or_exit = IntPrompt.ask("[green] Press 1: to start again. \n Press 2: to exit.")
            if player_restart_or_exit == 1:
                clear_screen()
                from main import main_quiz
                main_quiz()
            elif player_restart_or_exit == 2:
                exit()
            else:
                (console.print(":cross_mark:", "[red] INVALID OPTION", ":cross_mark:", "\n:cross_mark:", "[red] PLEASE TRY A 1 OR A 2", ":cross_mark:", style="bold", justify="center"))
                player_restart()
                raise AttributeError(player_restart())      
        except ValueError as ve:
            print(ve)