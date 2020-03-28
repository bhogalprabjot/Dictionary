#dictionary backend.

#to connect it to front end.
from Dictionary import *
#to access dictionary data file.
import json
#to check the similarity of a word in case of a wrong word.
import difflib
#gets the closest match to a word.
from difflib import get_close_matches

#open the json file.
data = json.load(open("data.json","r"))

#main funtion
def dict(word):

    #taking input from the user.
    words = word
    wordCheck(words.lower())

#function to check the a word in dictionary.
def wordCheck(words):
    simWord = get_close_matches(words,data)
    if words in data:
        print("%s - " %words)
        for item in data[words]:
            print(item)
            user_output(item)
    elif simWord:
        flag = input("Do you mean %s instead?(y/n)" %simWord[0])
        flag.lower()
        if flag == "y":
            wordCheck(simWord[0].lower())
        elif flag == "n":
            print("Sorry! Please try another word.")
            exit()
    else:

        print("No such word exists!")

# TODO: edit the program for GUI.
