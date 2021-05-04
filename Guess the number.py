# Run on codeskulptor
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

count=0

# helper function to start and restart the game

def new_game():
    global secret_number
    global count
    print "NEW GAME"
    print "choose the range"

# define event handlers for control panel
def range100():
    global secret_number
    secret_number=random.randrange(0,100)
    print "guess the number in between 0-100"
    
   
def range1000():
    global secret_number
    secret_number=random.randrange(0,1000)
    print "guess the number in between 0-1000"
           
        
def input_guess(guess):
    # main game logic goes here	
    global count
    g=int(guess)
    print "Guess was " + guess
    if count==7:
        print "You are out of guesses"
        print "-----------------------"
        count=0
        new_game()
    elif secret_number < g:
        print "Lower"
        count+=1
    elif secret_number > g:
        print "Higher"
        count+=1
    else:
        print "Correct!!"
        count=0
        new_game()

    
    
# create frame
frame=simplegui.create_frame("guess the number",200, 200)
frame.add_button("Range from 0 to 100", range100)
frame.add_button("Range from 0 to 1000", range1000)
guess=frame.add_input("Enter the guess", input_guess, 200)


# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()
