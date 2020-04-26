'''
Created on Apr 25, 2020

@author: ITAUser
'''
#import the random function
import random
#set variable keepPlaying to true
keepPlaying = True
#while keepPlaying is true:
while(keepPlaying):
    #print statement welcoming players to game
    print("Welcome to Rock, Paper, Scissors!")
    #print statement stating the rules (best 2 out of 3 Press 'q' to  quit)
    print("Best of 2 out of 3 wins! Press 'q' or 'Q' to quit any time")
    #make a key that assigns a number to each choice for the computer
    #(rock is 1, scissors is 2, paper is 3)
    '''
    1 = rock
    2 = scissors
    3 = paper
    '''
    
    #set computer's score to 0
    computerScore = 0
    #set player's score to 0
    playerScore = 0
    #while player's score is less than 2 and computer's score is less than 2:
    while(playerScore < 2 and computerScore < 2):
        #computer's choice = random number between 1 and 3
        computerChoice = random.randint(1,3)
        #player's choices = input(ask player to select Rock, Paper, or Scissors)
        choice = input("Please type rock, paper, or scissors:")
        choice = choice.lower()
        #if player inputs 'q' or 'Q':
        if(choice == "q"):
            # set keepPlaying to False
            keepPlaying = False
            #stop the loop
            break
            #else if (player inputs rock and computer chooses rock) or
            #(player inputs paper and computer chooses paper) or
            #(player inputs scissors andn computer chooses scissors):
        elif((choice == "rock" and computerChoice == 1) or (choice == "paper" and computerChoice == 3) or 
             (choice == "scissors" and computerChoice == 2)):
                #print out DRAW
            print("DRAW")
                #print out player's score and computer's score
            print("You:" + playerScore.__str__() + "CPU:" + computerScore.__str__())
            #else if (player inputs rock and computer chooses scissors) or
            #(player inputs scissors and computer chooses paper) or
            #(player inputs paper and computer chooses rock):
        elif((choice == "rock" and computerChoice == 2) or (choice == "scissors" and computerChoice == 3) or 
             (choice == "paper" and computerChoice == 1)):
                #add one to the player's score
            playerScore = playerScore + 1
                #print out player's score and computer's score
            print("You:" + playerScore.__str__() + " CPU:" + computerScore.__str__())
            #else if (player inputs rock and computer chooses paper) or
            #(player inputs scissors and computer chooses rock) or
            #(player inputs paper and computer chooses scissors):
        elif((choice == "rock" and computerChoice == 3) or (choice == "scissors" and computerChoice == 1) or 
             (choice == "paper" and computerChoice == 2)):
                #add one to the computer's score
            computerScore = computerScore + 1
                #print out player's score and computer's score
            print("You:" + playerScore.__str__() + "CPU:" + computerScore.__str__())
            #else:
                #tell the user their input was not valid
        else:
            print("Please type an acceptable option.")
#print statement thanking the players for playing
    print("Thanks for playing Rock, Paper, Scissors! It was fun.")
#if player's score is 2:
    if(playerScore == 2):
    #print statement letting the player know they won
        print("You won, congradulations!")  
#if computer's score is 2:
    if(playerScore == 2):
    #print statement letting the player know the computer won
        print("Sorry, you lost. CPU won by two points.")
#print out player's score and computer's score
    print("You:" + playerScore._str_() + "CPU:" + computerScore._str_())