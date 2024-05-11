<h1 style="text-align:center">T1A3 - Python Terminal Application - Quiz</h1>

<h2 style="text-align:center"> Table of Contents </h2>

- [Purpose](#purpose)
- [Code Styling Guide](#codeGuide)
- [Features](#Features)
- [Implementation Plan](#plan)
- [Installation](#Installation)


- [Links](#Links)
- [References](#References)
- [License](#License)
- [Badges](#Badges)

## <h2 style="text-align:center" id="purpose">Purpose</h2>

As a developer I need to show that I am able to design, implement and test a terminal application and demonstrate that I am able to use a range of developer tools so that I can prove my learning and understanding of the python and it's implementation.

Application Mandatory Requirements:

- Accept user input either in the form of a file or text input
- Produce printed output or ability to interact with the file system

## <h2 style="text-align:center" id="codeGuide">Code Styling Guide</h2>
My terminal application adheres to the PEP 8 Code Styling Guide which contributes to it's readability, maintainability and it's functionality.

<b>Here are 10 ways my project adheres to the PEP 8 Code Styling Guide:</b>

1. Indentation: 
    - Ise of 4 spaces for indentation
2. Whitespace: 
    - Appropriate whitespace use around operators and after commas.
3. Naming Conventions: 
    - Follow naming conventions for Variable/Function names.
4. Line Length: 
    - Maximum Line length of 79 characters or less.
5. Comments: 
    - The code includes comments to explain the purpose of functions, their parameters, and return values
6. Function Documentation: 
    - Docstrings used to document functions, purpose, parameters, and return values inline with PEP 257
7. Imports Formatting: 
    - Each import statement on own line, lineImports are grouped and organized at the top of the file.
8. String Formatting: 
    - E.g. f-strings or .format() is consistent.
9. Error Handling: 
    - Graceful error handling for exceptions e.g. KeyboardInterrupt.
10. Module Organization: 
    - Promoting modularity and maintainability by having code organized into different functionalities within separate modules.

## <h2 style="text-align:center" id="features">Features</h2>

<h3 style="text-align:center">Feature 1: Main Menu</h3>
<h4 style="text-align:center">Description</h4>

This is the main menu feature for ```menu_choice()``` it is the main entry point for the menu system.
This function will handle user input and will direct the pgoram flow based on the users choice.

<h4 style="text-align:center">Logic Walk Through</h4>
There are three options available.

 - Play Quiz
 - View Highscores
 - Exit Game

 This function starts with a ```try``` block that will handle the user input for any exceptions.
 
 Within the ```try``` block, there is an ```while True``` loop that will continue to display the menu choices until the user inputs a valid selection.

Inside of the ```while True``` loop, we get the user input through ```IntPrompt.ask("[green] Please input your choice ")``` this functionality has been through the use of the python rich library which has been used extensively throughout the application. Only a valid integer value input here will allow the applicaiton to proceed

Based on the users input:

- '1' will call the ```choice_one()``` function which will then proceed to play the quiz through it's executed code and function calls.
- '2' will call the ```choice_two()``` function which will then proceed which will then proceed to the view scoreboard option executing the applicable code and function calls.
- '3' will be the exit point of the applicaiton. This will print a message indicating that the user has selected to exit the program and then call the exit function.
- 'Anything else' will clear the screen and print a message indicating an invalid input and will loop through by continuing to display the ```quiz_header()``` and ```quiz_table()``` functions until the user has provided a valid input.

There is a ```KeyboardInterrupt``` event to catch exit errors and then gracefully exit the program.

<h4 style="text-align:center">Code Snippet - Menu Selection</h4>

```python
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
```
<br>
<br>
<h3 style="text-align:center">Feature 2: Scoring System</h3>
<h4 style="text-align:center">Description</h4>

This feature is a method within my ```class UserClass``` the purpose of this method ```save_highscores(self)``` is to take the users input at the end of the quiz and parse it into a ```highscores.csv``` CSV file.

<h4 style="text-align:center">Logic Walk Through</h4>

The ```save_highscores(self)``` method starts by opening the csv file in append mode. ```('a')```. This means that if the file doesn't exist it will be created. However if it does exist the newly saved data will be appended to it.

The method writes to the file with the ```with``` statement, inside a ```csv.writer``` object is then created to write the data to this file. This has been configured with the ```quoting=csv.QUOTE_NONNUMERIC``` this means that all non-numeric data e.g. strings and not integers will be quoted upon writing to the CSV file.

The ```writerow``` method is then called in the ```csv.writer``` object to write the single layer of data. This data consists of the following three elements:

- ```self.first_name```
- ```self.last_name```
- ```self.score```

The use of the ```with``` statement means that upon writing this data to the csv file it will then be properly closed , even in the event of an exception.

<h4 style="text-align:center">Code Snippet - Scoring System</h4>

```python
def save_highscores(self):
        with open ('highscores.csv', 'a',newline='') as f:
            write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            write.writerow([self.first_name, self.last_name, self.score])
        """
        FEATURE
        ----------
        This method saves the users data to the highscores.csv

        Parameters
        ----------
        None
        
        Returns
        ----------
        None
        """ 
```
<br>
<br>

<h3 style="text-align:center">Feature 3: User Input</h3>
<h4 style="text-align:center">Description</h4>

This feature is a function nameed ```get_user_input()``` this is a prompt function, the purpose of which is to prompt the user to enter a valid input integer value.

This is an imperative and reusable piece of code as its proved to be robust to be called multiple times in different capacities through the program.

<h4 style="text-align:center">Logic Walk Through</h4>

 This function starts with a ```try``` block that will handle the user input for any exceptions.

 Within the ```try``` block, is a prompt ```IntPrompt.ask("[green] Please enter the corresponding number: ")``` this message will be display in green and prpompt the user for an integer value to be input.

 If the user enters a ```KeyboardInterrupt``` the program will gracefully handle this and exit.
 If there is any other exception it will be caught within '''try''' block by the ```except Exception:```
 An error message will be display to indicate that the input was invalid. 
 On valid entry the screen will then be cleared and the function will return the integer value stored in the ```get_user_input()``` function.

<h4 style="text-align:center">Code Snippet - User Input</h4>

```python
def get_user_input():
    """
    Function will retrieve the user input.
    Parameters
    ----------
    None
        
    Returns
    ----------
    UserInput
        This will be the int value that corresponds with the users guess.
    """
    try:
        return IntPrompt.ask("[green] Please enter the corresponding number: ")
    except KeyboardInterrupt:
        exit()
    except Exception:
        console.print(":cross_mark:","[red] INVALID OPTION",":cross_mark:","\n:cross_mark:","[red] PLEASE TRY AGAIN",":cross_mark:" ,style="bold")
        clear_screen()
        return get_user_input()
```
<br>

## <h2 style="text-align:center" id="plan">Implementation Plan</h2>
<h3>Definition of Done</h3>

Functionality:
    - Program should be able to present questions to user and accept their answers.
    - Program should be able to accurately score the quiz based on user input and being correct or incorrect.
    - Program should be able to display the user score to them upon completing the quiz.
User Interface:
    - Program interfact should be clear and user friendly
    - Program should display questions and optional answers legibly.
    - Program should provide instructions where neccessary
Code Quality:
    - Python code should adhere to PEP8 coding standards
    - Code should be organized into seperate classes/functions as required.
    - Program should have appropriate functional error handling
Quiz Content:
    - Questions should be unambiguous
    - Questions should be well-written
    - Appropriate multiple choice answers provided
Documentation:
    - Clear appropriate documention
    - How to run the program, required dependencies
Submission:
    - Assignment submitted in correct format as required by assignment.
    - Meet any additionally provided requirements

<h3>EPIC: Feature 1 - menu_choice()</h3>

This checklist forms a high level overview of the development steps completed for the creation of this feature.

<h4>Checklist</h4>

    [x] Project Environment
    [x] Create main script
    [x] Implement menu display
    [x] Implement choice functionality
    [x] Implement error handling
    [x] Implement screen clearing
    [x] Enhance the user interface
    [x] Documentation


<h3>EPIC: Feature 2: - save_highscores()</h3>

This checklist forms a high level overview of the development steps completed for the creation of this feature.

<h4>Checklist</h4>

    [x] Project Environment
    [x] Create class and attributes
    [x] Immplement csv handling function
    [x] Implement save_highscores() method
    [x] Implement screen clearing
    [x] Documentation

<h3>EPIC: Feature 3: - get_user_input()</h3>

<h4>Checklist</h4>

This checklist forms a high level overview of the development steps completed for the creation of this feature.

<h3>Checklist</h3>

    [x] Project Environment
    [x] Create the function
    [x] Research the rich library and implementation
    [x] Integrate the 'prompt' utility
    [x] Implement error handling
    [x] Documentation


<h2 style="text-align:center">Trello Board</h2>
On my Trello board which I have used for the project management of the three features implementation. 

Conventions Used:

- Each feature is an Epic identified by the labels provided to the user stories.
- Within each Epic each story is prioritized according to requirements of the feature
- A fourth label epic for cross-stories over the features.
- Columns for:
    - Backlog
    - To-Do
    - Blockers
    - Done

<h3 style="text-align:center">Trello Board Link</h3>
<a href="https://trello.com/b/itrSmKJq">Terminal Application - T1A3</a>

<h2 style="text-align:center">Trello Board - Screenshots</h2>

## <h2 style="text-align:center" id="installation">Installation</h2> 
Steps to run.
- steps to install the application
- any dependencies required by the application to operate
- how to use any command line arguments made for the application


<h2>System/Hardware Requirements</h2>

<h3>System Requirements</h3>
- Operating System (OS)that supports Python 3.0 or higher. (MacOS, Linux, Windows)

<h3>Hardware Requirements</h3>
- 70 MB of free disk space
- 512 MB of RAM


## <h2 style="text-align:center" id="Links"> Links</h2>
Github Repository:
    <br>- <a href ="https://github.com/SpencerBadger/T1A3-Terminal-Application">T1A3-Terminal-Application</a>

Trello Board:
    <br>- <a href="https://trello.com/b/itrSmKJq">Terminal Application - T1A3</a>

## <h2 style="text-align:center" id="credits"> References</h2>

Selatha (2024) The (almost) ultimate wow quiz, ProProfs. Available at: <a href="https://www.proprofs.com/quiz-school/story.php?title=almost-ultimate-wow-quiz">Ultimate Wow Quiz</a> (Accessed: 02 May 2024). 

van Rossum, G., Warsaw, B., & Coghlan, A. (2001, July 5). PEP 8 – style guide for python code. Python Enhancement Proposals (PEPs). <a href="https://peps.python.org/pep-0008/">PEP 8 - STyle Guide</a> 

## <h2 style="text-align:center">License</h2>
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## <h2 style="text-align:center">Badges</h2>
![GitHub followers](https://img.shields.io/github/followers/SpencerBadger?style=social)
![GitHub User's stars](https://img.shields.io/github/stars/SpencerBadger?style=social)

<img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white" />

<img alt="Bash" src="https://img.shields.io/badge/-Made%20with%20Bash-1f425f.svg?style=for-the-badge&logo=bash&logoColor=white"/>


![Profile View Counter](https://komarev.com/ghpvc/?username=SpencerBadger)


![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=SpencerBadger&show_icons=true)