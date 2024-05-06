import rich
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import print

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
        for question in questions:
            
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------")
            console.print("[green]" + question)
            console.print("[white]---------------------------------------------------------------------------------------------------------------------------------")

            for answer in multiple_choice[question_number]:
                
                print(answer)
            guesses = input("Please enter the corresponding letter: ").upper()
            data_table[0].append(questions[question_number])
            data_table[1].append(long_answer[question_number])
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
        console.print(table)

#    SAVED USERS DETAILS AND SCORE
        console.print("[white]---------------------------------------------------------------------------------------------------------------------------------")
        yes = console.input("[green] Would you like to save your results? (Y/N)").upper()
        if yes == "Y":
            user_record(score)
        elif yes == "N":       
            exit()



def user_record(score):
    first_name = str(input("Please provide your first name: "))
    last_name =str(input("Please provide your last name: "))
    user_details = {"First Name ":first_name,"Last Name ":last_name,"Score" : score}
    print(user_details)
    with open('scoreboard.json','w') as f:
             json.dump(user_details, f, indent=4)
        return(None)
    