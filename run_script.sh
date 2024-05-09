#!/bin/bash
if [[ -x "$(command -v python)" ]];
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]];
    then 
        read -p "Would you like to play the quiz? Any required dependencies will be installed. Press Y to continue (Y/N)?: " answer
        if [[ $answer == [Yy] ]];
        then
            pip install -r ./requirements.txt
            python3 main.py
        else
            echo 'You will need to install the required dependencies before playing.'
            echo 'Please run this script again to continue.' >&2
            exit 1
        fi
    else
        echo "Please run this script again when you are ready to install the required dependencies" >&2
    fi
else
    echo 'Error: '
    echo 'This program runs on Python 3, please update accordingly' >&2 
    echo 'To install Python, check out https://installpython3.com/' >&2
    exit 1 
fi