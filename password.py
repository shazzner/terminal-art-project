#!/usr/bin/python

import pyttsx, signal, os, time
#pip install git+https://github.com/pwaller/pyfiglet
# pyEnchant for spellchecking (seeing if it's an english word)
# import enchant
# d = enchant.Dict("en_US")
# d.check(pswd)
from pyfiglet import Figlet
asciiText = Figlet(font='slant')


# Disable ctrl-c, ctrl-z
#signal.signal(signal.SIGINT, signal.SIG_IGN)
#signal.signal(signal.SIGTSTP, signal.SIG_IGN)

# Main

# Show Password Prompt
# Wait for Input

pyttsx = pyttsx.init("espeak", True)
rate = pyttsx.getProperty('rate')
pyttsx.setProperty('rate', rate-500)
pyttsx.setProperty('volume', 0.5)

actionQueue = []

def addASCIIWord(string):
    return False

def flashWord(string):
    for x in range(0,6):
        print asciiText.renderText(string)
        print " "

def sayWord(string):
    pyttsx.say(string)
    pyttsx.say(" ")

def addClear():
    os.system('clear')
    

while True:
    pyttsx.say("Enter Password")
    pyttsx.say(" ")
    pyttsx.runAndWait()
    
    pswd = raw_input("Password: ")
    if pswd:        

        if pswd == 'adminoverride':
            exit()

        if '!' in pswd:
            pyttsx.setProperty('volume', 1.0)
            actionQueue.append( ("flashWord", "! Means Louder") )
            actionQueue.append( ("sayWord", "Oh did you want it louder?") )

        pyttsx.say(pswd)
        pyttsx.say(" ")
        pyttsx.runAndWait()
        pyttsx.say(" ")
            
        list_ = ['admin', 'root', 'administrator']
        if any(word in pswd for word in list_):
            actionQueue.append( ("sayWord", "Warning") )
            actionQueue.append( ("flashWord", "Warning") )
            actionQueue.append( ("sayWord", "Warning") )

        list_ = ['pussy', 'cock', 'ass', 'bitch', 'cunt', 'dick']
        if any(word in pswd for word in list_):
            actionQueue.append( ("sayWord", "That was naughty") )
            actionQueue.append( ("flashWord", "Naughty") )
            actionQueue.append( ("sayWord", "That was naughty") )
            
        list_ = ['damn', 'fuck', 'shit']
        if any(word in pswd for word in list_):
            actionQueue.append( ("sayWord", "Kiss your mother") )
            actionQueue.append( ("flashWord", "YOUR MOM") )
            actionQueue.append( ("sayWord", "With your mouth") )

        if '@' in pswd:
            actionQueue.append( ("sayWord", "at symbol") )
            actionQueue.append( ("flashWord", "@ @ @ @ @ @") )
            actionQueue.append( ("sayWord", "where are you at") )

        if '&' in pswd:
            actionQueue.append( ("sayWord", "And") )
            actionQueue.append( ("flashWord", "& What?") )
            actionQueue.append( ("sayWord", "and what") )

        if 'help' in pswd:
            actionQueue.append( ("sayWord", "Help Computer") )
            actionQueue.append( ("flashWord", "Help Computer") )
            actionQueue.append( ("sayWord", "Help Computer") )
            
        # Run Through Queue
        for event,value in actionQueue:

            if "flashWord" in event:
                flashWord(value)
                pyttsx.say(" ")

            if "sayWord" in event:
                sayWord(value)

            pyttsx.runAndWait()
        
            
    else:
        pyttsx.say("You did not enter a password!")
        pyttsx.say(" ")
        pyttsx.runAndWait()

    # Clear Queue
    actionQueue = []
    pyttsx.setProperty('volume', 0.5)
    os.system('clear')
    time.sleep(1)
    
# User my type a password in
# When user presses enter

# Read Password
# Does the Password?

# Is the password 'adminoverride' ?
# If so, let's quit out of the program

# Otherwise:

# Have any words in it?
# Does in include certain words?
# Have any symbols in it?
# Does it have any spaces in it?
# Let's add an event based on what got typed in

# Iterate through all events

# Go back to the password prompt
