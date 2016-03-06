#!/usr/bin/python

import pyttsx, signal, os, time
from random import randint

# Pip install command for Figlet:
# pip install git+https://github.com/pwaller/pyfiglet

# pyEnchant for spellchecking (seeing if it's an english word)
import enchant
from pyfiglet import Figlet
asciiText = Figlet(font='slant')

# Disable ctrl-c, ctrl-z
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)

pyttsx = pyttsx.init("espeak", True)
rate = pyttsx.getProperty('rate')
pyttsx.setProperty('rate', rate-500)
pyttsx.setProperty('volume', 0.5)

d = enchant.Dict("en_US")

actionQueue = []

def flashWord(string):
    for x in range(0,4):
        print asciiText.renderText(string)
        print " "

def sayWord(string):
    pyttsx.say(string)
    pyttsx.say(" ")

def addClear():
    os.system('clear')
    
while True:
    print "BBZed Micron Super System"
    print "Copyright 1983 by SHAZZNER"
    print "ROM: 64k RAM: 64k MEM USAGE: "+str(randint(1,3))+str(randint(0,9))+"k"
    print "LOGIN: USER"
    pyttsx.say("Enter Password")
    pyttsx.say(" ")
    pyttsx.runAndWait()
    
    pswd = raw_input("PASSWORD: ")
    if pswd:        

        if pswd == '123adminoverride':
            exit()

        if len(pswd) > 12:
            actionQueue.append( ("flashWord", "Too Long" ) )
            pyttsx.say("Your password is too long")
            pyttsx.say(" ")
            pyttsx.runAndWait()
            pyttsx.say(" ")
            
        else:

            if '!' in pswd:
                pyttsx.setProperty('volume', 1.0)
                actionQueue.append( ("flashWord", "! Means Louder") )
                actionQueue.append( ("sayWord", "Oh did you want it louder?") )

            for x in range(0,4):
                print asciiText.renderText(pswd)
                print " "
            pyttsx.say(pswd)
            pyttsx.say(" ")
            pyttsx.runAndWait()
            pyttsx.say(" ")

            # Doesn't work so well, should strip out special characters
            if not d.check(pswd):
                pyttsx.say("That's not even a real word")
                pyttsx.say(" ")
                pyttsx.runAndWait()
            
            list_ = ['admin', 'root', 'administrator']
            if any(word in pswd for word in list_):
                actionQueue.append( ("flashWord", "Warning") )
                actionQueue.append( ("sayWord", "Warning") )
                actionQueue.append( ("flashWord", "Nice Try") )
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

            if '*' in pswd:
                actionQueue.append( ("flashWord", "* <- star") )
                actionQueue.append( ("sayWord", "Seeing Stars") )

            if '^' in pswd:
                actionQueue.append( ("flashWord", "=^.^=") )
                actionQueue.append( ("sayWord", "Kitty Cat") )

            if '$' in pswd:
                actionQueue.append( ("flashWord", "Capitalism") )
                actionQueue.append( ("sayWord", "Deep Meaning") )

            if '#' in pswd:
                actionQueue.append( ("sayWord", "Hash tag") )
                actionQueue.append( ("flashWord", "#Hashtag") )
                actionQueue.append( ("sayWord", "Pop culture reference") )

            if '%' in pswd:
                actionQueue.append( ("sayWord", "Sweet Pea") )
                actionQueue.append( ("flashWord", "Don't Ask") )
                actionQueue.append( ("sayWord", "Bubble Gum") )
            
            # Run Through Queue
            for event,value in actionQueue:

                if "flashWord" in event:
                    flashWord(value)
                    pyttsx.say(" ")

                if "sayWord" in event:
                    sayWord(value)

                # Just in case
                pyttsx.say(" ")
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
    
