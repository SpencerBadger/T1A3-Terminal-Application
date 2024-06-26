<h1 style="text-align:center">T1A3 - Python Terminal Application - Quiz</h1>

<h2 style="text-align:center">Table of Contents</h2>

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
<details>
<summary><b>Here are 10 ways my project adheres to the PEP 8 Code Styling Guide:</b></summary>

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
</details>

## <h2 style="text-align:center" id="features">Features</h2>
<details>
<summary><h3 style="text-align:center">Feature 1: Main Menu</h3></summary>
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
</details>
<details>
<summary><h4 style="text-align:center">Code Snippet - Menu Selection</h4></summary>

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

</details>
<br/>
<details>
<summary><h3 style="text-align:center">Feature 2: Scoring System</h3></summary>
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

</details>
<details>
<summary><h4 style="text-align:center">Code Snippet - Scoring System</h4></summary>

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

</details>

<br/>

<details>
<summary><h3 style="text-align:center">Feature 3: User Input</h3></summary>
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
 </details>
<details>
<summary><h4 style="text-align:center">Code Snippet - User Input</h4></summary>

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

</details>

<br/>


## <h2 style="text-align:center" id="plan">Implementation Plan</h2>
<h3>Definition of Done</h3>
<details>
<summary>Functionality:</summary>

    - Program should be able to present questions to user and accept their answers.
    - Program should be able to accurately score the quiz based on user input and being correct or incorrect.
    - Program should be able to display the user score to them upon completing the quiz.
</details>
<details>
<summary>User Interface:</summary>

    - Program interface should be clear and user friendly
    - Program should display questions and optional answers legibly.
    - Program should provide instructions where neccessary
</details>
<details>
<summary>Code Quality:</summary>

    - Python code should adhere to PEP8 coding standards
    - Code should be organized into seperate classes/functions as required.
    - Program should have appropriate functional error handling
</details>
<details>
<summary>Quiz Content:</summary>

    - Questions should be unambiguous
    - Questions should be well-written
    - Appropriate multiple choice answers provided
</details>
<details>
<summary>Documentation:</summary>

    - Clear appropriate documention
    - How to run the program, required dependencies
</details>
<details>
<summary>Submission:</summary>

    - Assignment submitted in correct format as required by assignment.
    - Meet any additionally provided requirements
</details>
<details>
<summary><h3>EPIC: Feature 1 - menu_choice()</h3></summary>

A high level overview of the development steps completed for the creation of this feature.

<h4>Checklist</h4>

    [x] Project Environment
    [x] Create main script
    [x] Implement menu display
    [x] Implement choice functionality
    [x] Implement error handling
    [x] Implement screen clearing
    [x] Enhance the user interface
    [x] Documentation
</details>
<details>
<summary><h3>EPIC: Feature 2: - save_highscores()</h3></summary>

A high level overview of the development steps completed for the creation of this feature.

<h4>Checklist</h4>

    [x] Project Environment
    [x] Create class and attributes
    [x] Immplement csv handling function
    [x] Implement save_highscores() method
    [x] Implement screen clearing
    [x] Documentation
</details>
<details>
<summary><h3>EPIC: Feature 3: - get_user_input()</h3></summary>

<h4>Checklist</h4>

A high level overview of the development steps completed for the creation of this feature.

    [x] Project Environment
    [x] Create the function
    [x] Research the rich library and implementation
    [x] Integrate the 'prompt' utility
    [x] Implement error handling
    [x] Documentation
</details>

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

<h2 style="text-align:center">Epics and User Stories | Deadlines and Duartions</h2>

<details>
<summary><h3>DAY 1 - 3 | 03 May 24 - 05 May 24</h3></summary>
<details>
<summary>EPIC: Cross Feature Stories | As a developer I want to document the program and refractor the code for clarity and adherence to the PEP8 code style so that there is appropriate code quality and readability.</summary>

    Acceptance Criteria:
        PEP8 Standards Met
        DRY standards met
        Docstrings Correctly met.
</details>

<details>
<summary>EPIC: Cross Feature Stories | As a developer I want to implement error handling to handle invalid input gracefully, so that the program doesn't crash and the user has a seamless experience.</summary>

    Acceptance Criteria:
        Program handles invalid input
        Provides appropriate feedback
</details>
<details>
<summary>EPIC: Cross Feature Stories | As a developer I want to setup the correct project directory structure, initilize version control and establish a virtual environment so that I can work with an organized development environment efficiently.</summary>

    Acceptance Criteria:
        Folders Correctly Established
        Repository Established
        .venv installed and active
</details>

<details>
<summary>EPIC: Cross Feature Stories | As a developer perform testing of program so that I can ensure that all features work and meet correct standards.</summary>

    Acceptance Criteria:
        Test Repeatedly
        Test Frequently
        Correct any issues
</details>
<details>
<summary>EPIC: menu_choice() | As a developer I want to create the main script for the menu feature so that I can implement the main logic.</summary>

    Acceptance Criteria:
        main.py created and holding the menu selection code.

</details>

</details>

<details>
<summary><h3>DAY 4 - 6 | 06 May 24 - 08 May 24</h3></summary>
<details>
<summary>EPIC: get_user_input() | As a developer I need to create and integrate the prompt utility from rich so that users are able to input valid data.</summary>

    Acceptance Criteria:
        Correctly coded
        Correctly integrated code
        Retrieves user data and allocates it accordingly.

</details>
<details>
<summary>EPIC: menu_choice() | As a developer I want to utilize external libraries to enhance the visual appearance so that it is both appealing and and user-friendly.</summary>

    Acceptance Criteria:
        Extensive use of rich
        Use of pyglet

</details>

<details>
<summary>EPIC: save_highscores() | As a developer I want to create a CSV file name "highscores.csv" with appropriate headers being ("First Name", "Last Name", "Score") so that I have a structured format within which to store/save the users scores.</summary>

    Acceptance Criteria:
        highscores.csv created
        Headers created - First Name, Last Name, Score

</details>
<details>
<summary>EPIC: save_highscores() | As a developer I want to integrate the save_highscores method into the game logic so that I can ensure high scores are saved correctly without interruption to the game flow.
</summary>

    Acceptance Criteria:
        Call on the method with dummy data.
        Test to ensure appropriate calls and returns work correctly.
        Check csv to ensure data is saved correctly.

</details>
</details>

<details>
<summary><h3>DAY 7 - 9 | 09 May 24 - 11 May 24</h3></summary>
<details>
<summary>EPIC: save_highscores() | As a developer I want to create and implement a class and method for saving scores so that I can ensure the method works as expected.</summary>

    Acceptance Criteria:
        Create a class
        Create a method
        Test with dummy data

</details>
<details>
<summary>EPIC: save_highscores() | As a developer I want to implement error handling for the file operations and validate the user input before writing to csv so that I can prevent potential issues from arising and ensure appropriate data integrity.</summary>

    Acceptance Criteria:
        Error Handling Integrated
        Tested to ensure data integrity

</details>
<details>
<summary>EPIC: menu_choice() | As a developer I want to be able to see a menu displayed so that a user can choose an option.</summary>

    Acceptance Criteria:
        Ability to see a menu
        Ability to select an option

</details>


<details>
<summary>EPIC: menu_choice() | As a developer I want to implement the ability to select different options in the menu so that a user can use the program.</summary>

    Acceptance Criteria:
        Able to see different options
        Able to have user input to select different options.

</details>
</details>







## <h2 style="text-align:center" id="installation">Installation</h2> 
<details>
<summary><h3>Installation Steps</h3></summary>

(1) Clone the github repository:

Open your terminal or command prompt
navigate to the directory on your device where you want to clone the repository
use the following command to clone the repository

```sh
git clone https://github.com/SpencerBadger/T1A3-Terminal-Application.git
```
(2) Navigate to the repository directory:

Once the cloning is complete use the `cd` command to navigate into the repository

```sh
cd T1A3-Terminal-Application
```
(3) Execute the shell script:

Check if the `run_script.sh` file correclty exists in the repository using the `ls` command

```sh
ls
```

If you see the `run_script.sh` file you can execute it using the following command:

```sh
bash run_script.sh
```

or 

```sh
./run_script.sh
```
(4) Complete Installation Steps:

The `run_script.sh` will check if your system has `python3` installed.

If it is installed it will prompt advise that to play the quiz you will need to install all required dependencies.

Upon enterering `y` a `python` virtual environment will be started and/or installed. Following which the dependencies will be installed into that virtual environment.

(5) Play the game and have fun.

</details>

<details>
<summary><h3>Dependencies</h3></summary>

```python
astunparse==1.6.3
chardet==5.2.0
colorama==0.4.6
exceptiongroup==1.2.1
iniconfig==2.0.0
Jinja2==3.1.4
markdown-it-py==3.0.0
MarkupSafe==2.1.5
mdurl==0.1.2
numpy==1.26.4
packaging==24.0
pandas==2.2.2
pdoc==14.4.0
pluggy==1.5.0
pyfiglet==0.7.5
Pygments==2.17.2
python-dateutil==2.9.0.post0
pytz==2024.1
rich==13.7.1
six==1.16.0
tomli==2.0.1
tzdata==2024.1
```
</details>



<h2>System/Hardware Requirements</h2>


<details>
<summary><h3>System Requirements</h3></summary>

    - Operating System (OS)that supports Python 3.0 or higher. (MacOS, Linux, Windows)
</details>

<details>
<summary><h3>Hardware Requirements</h3></summary>

    - 70 MB of free disk space
    - 512 MB of RAM
</details>
</details>

## <h2 style="text-align:center" id="Links"> Links</h2>

Github Repository:
    <br>- <a href ="https://github.com/SpencerBadger/T1A3-Terminal-Application" target="_blank">T1A3-Terminal-Application</a>

Trello Board:
    <br>- <a href="https://trello.com/b/itrSmKJq" target="_blank">Terminal Application - T1A3</a>


## <h2 style="text-align:center" id="credits"> References</h2>

Selatha (2024) The (almost) ultimate wow quiz, ProProfs. Available at: <a href="https://www.proprofs.com/quiz-school/story.php?title=almost-ultimate-wow-quiz">Ultimate Wow Quiz</a> (Accessed: 02 May 2024). 

van Rossum, G., Warsaw, B., & Coghlan, A. (2001, July 5). PEP 8 – style guide for python code. Python Enhancement Proposals (PEPs). <a href="https://peps.python.org/pep-0008/">PEP 8 - STyle Guide</a> (Accessed: 02 May 2024)

## <h2 style="text-align:center">License</h2>
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## <h2 style="text-align:center">Badges</h2>
![GitHub followers](https://img.shields.io/github/followers/SpencerBadger?style=social)
![GitHub User's stars](https://img.shields.io/github/stars/SpencerBadger?style=social)

<img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white" />

<img alt="Bash" src="https://img.shields.io/badge/-Made%20with%20Bash-1f425f.svg?style=for-the-badge&logo=bash&logoColor=white"/>


![Profile View Counter](https://komarev.com/ghpvc/?username=SpencerBadger)


![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=SpencerBadger&show_icons=true)