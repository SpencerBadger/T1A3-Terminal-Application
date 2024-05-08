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

console = Console()
table = Table()
data_table = [[],[],[],[]]

def question_quiz_warcraft():
        
        questions = ("1. What is the name of the human capital city in World of Warcraft?",
                "2. Which of these classes are available to blood elves in World of Warcraft?",
                "3. Which four-wing instance located in Tirisfal Glades is frequently farmed by players in World of Warcraft?",
                "4. Who built Karazhan in World of Warcraft?",
                "5. What is the draenei racial heal called in World of Warcraft?" )

        multiple_choice = (("A. Ironforge", "B. Elwynn City", "C. Stormwind City", "D. Silvermoon City", "E. Booty Bay"),
                ("A. Warrior", "B. Warlock", "C. Priest", "D. Hunter","E. Rogue","F. All of the above"),
                ("A. Scarlet Monastery", "B. Auchindoun", "C. The Stockade", "D. Shadowfang Keep","E. The Deadmines"),
                ("A. Archimonde","B. Prince Kael'thas Sunstrider", "C. Guardian Aegwynn", "D. Kel'thuzad","E. Arthas Menethil"),
                ("A. Blessing of Argus", "B. Gift of the Naaru", "C. Symbol of Hope", "D. Velen's Touch","E. Call of the Exodar"))
        
        answers = ("C","F","A","C","B")
        long_answer =("C. Stormwind City","F. All of the above","A. Scarlet Monastery","C. Guardian Aegwynn","B. Gift of the Naaru")
        guesses = []
        question_number = 0
        score = 0
        'Loops for questions'
        for question in questions:
            os.system('cls' if os.name == 'nt' else 'clear')
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
            console.print("[green]" + question, justify="center")
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")

            for answer in multiple_choice[question_number]:
                console.print(answer, justify="center")
    
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------", justify="center")
            
            try:
                guesses = Prompt.ask("[green] Please enter the corresponding letter: ").upper()
            except va 
            except KeyboardInterrupt:
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exit()
                except SystemExit:
                    os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')
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
                os.system('cls' if os.name == 'nt' else 'clear')
                what_next_next = IntPrompt.ask("[green] Press 1: to start again. \n Press 2: to exit.")
                if (what_next_next == 1):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    from main import main_quiz
                    main_quiz()
                elif(what_next_next == 2):
                    exit()
            else:
                console.print(":cross_mark:","[red] INVALID OPTION",":cross_mark:","\n:cross_mark:","[red] PLEASE TRY AGAIN",":cross_mark:" ,style="bold")
def write_data(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    first_name = str(input("Please provide your first name: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    last_name =str(input("Please provide your last name: "))
    user_details = UserClass(first_name,last_name,score)
    user_details.show()
    user_details.save_highscores()
    


    

