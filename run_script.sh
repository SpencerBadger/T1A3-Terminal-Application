#!/bin/bash
#                                Bash Script                                    #
#       This template is for running the quiz I created in python.              #
#                                                                               #
#       Change History:                                                         #
#       09/05/24 Spencer Badger -   Original Code.Bash Created.                 #
#################################################################################
#Checking if python is installed
VENV_NAME=".venv"

if [[ -x "$(command -v python)" ]];
then
    #If python is installed and the version correct.
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]];
    #If the version is correct, then check the user is happy to have the dependencies installed.
    then 
        read -p    "Would you like to play the quiz? Any required dependencies will be installed. Press Y to continue (Y/N)?: " answer
        if [[ $answer == [Yy] ]];
        #If they selected yes then proceed to check, setup the virtual enviroment and then install dependencies from the requirements.txt
        then
            if [ ! -d "$VENV_NAME" ];
                then
                    echo "Creating virtual environment.">&2
                    python3 -m venv $VENV_NAME
                fi
            echo "Activating virtual environment.">&2
            source $VENV_NAME/bin/activate
            echo "Installing dependencies">&2
            pip install -r ./requirements.txt
            echo "Dependencies installed.">&2
            python3 main.py   
        else
            #If user not happy to install the dependencies they will be notified and advised to run the bash script again when they are.
            echo 'You will need to install the required dependencies before playing.'>&2
            echo 'Please run this script again to continue.' >&2
            exit 1
        fi
    else
        echo "Please run this script again when you are ready to update to the required version of Python." >&2
        exit 1
    fi   
else
    echo 'Error: '
    echo 'This program runs on Python 3, please update accordingly' >&2 
    exit 1 
fi