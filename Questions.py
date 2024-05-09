"""
This module contains various data relating to the quiz questions/answers logic for the quiz.
"""
import rich, pyfiglet, colorama, os
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import print
from userclass import *
from rich.prompt import IntPrompt, Prompt
from os import system, name

console = Console()
table = Table()
data_table = [[],[],[],[]]

def question_quiz_warcraft():
        
        questions = ("1. What is the name of the human capital city in World of Warcraft?",
                "2. Which of these classes are available to blood elves in World of Warcraft?",
                "3. Which four-wing instance located in Tirisfal Glades is frequently farmed by players in World of Warcraft?",
                "4. Who built Karazhan in World of Warcraft?",
                "5. What is the draenei racial heal called in World of Warcraft?" )

        multiple_choice = (("1. Ironforge", "2. Elwynn City", "3. Stormwind City", "4. Silvermoon City", "5. Booty Bay"),
                ("1. Warrior", "2. Warlock", "3. Priest", "4. Hunter","5. Rogue","6. All of the above"),
                ("1. Scarlet Monastery", "2. Auchindoun", "3. The Stockade", "4. Shadowfang Keep","5. The Deadmines"),
                ("1. Archimonde","2. Prince Kael'thas Sunstrider", "3. Guardian Aegwynn", "4. Kel'thuzad","5. Arthas Menethil"),
                ("1. Blessing of Argus", "2. Gift of the Naaru", "3. Symbol of Hope", "4. Velen's Touch","5. Call of the Exodar"))
        
        answers = (3,6,1,3,2)
        long_answer =("C. Stormwind City","F. All of the above","A. Scarlet Monastery","C. Guardian Aegwynn","B. Gift of the Naaru")
        guesses = []
        question_number = 0
        score = 0
        #Loops for questions
        for question in questions:
            clear_screen()
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
            console.print("[green]" + question, justify="center")
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")

            for answer in multiple_choice[question_number]:
                console.print(answer, justify="center")
    
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
            
            try:
                guesses = IntPrompt.ask("[green] Please enter the corresponding number: ")
            except KeyboardInterrupt:
                try:
                    clear_screen()
                    exit()
                except SystemExit:
                    clear_screen()
                    exit()
            'Error handling for incorrect choices'
            data_table[0].append(questions[question_number])
            data_table[1].append(long_answer[question_number])
            'Appending the data table for presenting the scores and saving the results'
            if guesses == answers[question_number]:
                score += 1
                print("Score")
                console.print(":white_check_mark:" + "[green] Correct!", justify="center")
                data_table[2].append("Correct")
                data_table[3].append(score)
            else:
                console.print(":cross_mark:" + "[red] Incorrect!", justify="center")
                data_table[2].append("Incorrect")
            
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------")
            
            question_number += 1
        clear_screen()
        console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
        table = Table(title = "Results",show_lines=True)
        table.add_column("Question", justify="left")
        table.add_column("Answer", justify="left")
        table.add_column("Correct/Incorrect", justify="left")
        table.add_column("Score", justify="left")
        for i in range(len(data_table[0])):
            if data_table[2][i] == "Correct":
                table.add_row(data_table[0][i],data_table[1][i],"[green] Correct",":white_check_mark:")
            else:
                 table.add_row(data_table[0][i],data_table[1][i],"[red] Incorrect",":cross_mark:")
        table.add_row("Total Score: ","","",str(score))
        console.print(table,justify="center")
 
#    SAVED USERS DETAILS AND SCORE
        console.print("[white]---------------------------------------------------------------------------------------------------------------------------------",justify="center")
        while True:
            what_next = IntPrompt.ask("[green] Would you like to save your results? \n Press (1) to save \n Press (2) to skip saving \n")
            if(what_next == 1):
                write_data(score)
                input("Press Enter to continue...")    
                from main import menu_choice
                menu_choice() 
            elif(what_next == 2):
                clear_screen()
                what_next_next = IntPrompt.ask("[green] Press 1: to start again. \n Press 2: to exit.")
                if (what_next_next == 1):
                    clear_screen()
                    from main import main_quiz
                    main_quiz()
                elif(what_next_next == 2):
                    exit()
            else:
                console.print(":cross_mark:","[red] INVALID OPTION",":cross_mark:","\n:cross_mark:","[red] PLEASE TRY AGAIN",":cross_mark:" ,style="bold")
                
def write_data(score):
    clear_screen()
    first_name = str(input("Please provide your first name: "))
    clear_screen()
    last_name =str(input("Please provide your last name: "))
    user_details = UserClass(first_name,last_name,score)
    user_details.show()
    user_details.save_highscores()
    
def clear_screen():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')

    

