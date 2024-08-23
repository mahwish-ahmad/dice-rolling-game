"""
Created on Sat Nov 11 13:36:30 2023

@author: Mahwish 

Problem Description:
    
Write a program that plays a simple game of guess the sum of two dice. In this game, 
the user plays against the computer. The computer generates the sum and the user must 
guess the number. There are 5 rounds and the user gets 3 guesses to guess the number.
He/she must also be given hints as to whether the number is higher or lower than the
user's guess. If the user gets the number right on the first guess, they get 30 points.
If they get it right on the second, they get 20 and on the third, 10. If the user 
does not get the number right at all, they get no points. Create a scoreboard file
and update the user's score after each round. They should also be asked if they wish
to play again. 

"""

import random # Import the random module to generate random numbers for the guessing game

def rollDice(): # This function adds the sum of the two dice and returns the number to be compared
    rand = random.randint
    return rand(1,6) + rand(1,6)

def score(guessLeft): 
    
# This function calculates + returns the score based on the amount of guesses the user has remaining

    score = 0 # Initialize the score to 0
    if guessLeft == 3:
        score += 30 # Adds the value to the score
    elif guessLeft == 2:
        score += 20
    elif guessLeft == 1:
        score += 10
    else:
        score = 0
        
    return score # Return the score to the playRound() function

def playRound(x): # This function plays each of the 5 rounds and returns the current score

    guesses = 3 # Initialize the current guesses to 3 (that is how many the user starts with)
    currentScore = 0 # Initialize the current score to 0
    computerGuess = rollDice() # Get the random number that the computer selected
    file = open("Scorekeeper.txt", "a") # Open the file with append to update the user's scores
    
    while guesses > 0: # Create a while loop that runs until the user has no guesses left
        
        try: # Use exception handling to ensure the user enters an integer
            userGuess = int(input("Guess the roll: ")) # Ask the user for their answer
            if userGuess not in range(2,13): # Ensure the number is in the range 2-12
                print("Make sure you enter a number between 2-12")
        except ValueError:
            print("Make sure you are entering an integer!!") # Display the error to the user
        
        if userGuess == computerGuess: # If the user gets the number right, calculate their score
            currentScore = score(guesses) 
            
            print(f"Horray! You earned {currentScore} points") # Display the score
            file.write(f"\nRound {x}: You scored {currentScore} points!\n") # Write the score to the file
            
            break # Use a break to exit the loop as the user got the number right
        else:
            guesses -= 1 # Decrement guesses by 1
            
            # Give the user hints as to whether the number is higher or lower than their current guess
            if userGuess > computerGuess: 
                print("The number should be lower!")
            if userGuess < computerGuess:
                print("The number should be higher")
            if guesses > 1:
                print(f"Wrong! {guesses} guesses left.") # Tell the user how many guesses are left
            else:
                print(f"Wrong! {guesses} guess left.")

    if currentScore == 0: # If the user does not have any points, tell them and write to the file
        print(f"Sorry, you don't get any points. The correct answer was {computerGuess}") 
        file.write(f"\nRound {x}: You scored no points!\n") 
    
    file.close() # Close the file
    return currentScore # Return the score to the main function

def main(): # This is the main function that plays the game
    
    totalScore = 0 # Initialize the total score to 0

    for x in range (1, 6): # Create a for loop to iterate 5 times for the 5 rounds
        print()
        totalScore += playRound(x) # Play the round and also keep track of the total score

    file = open("Scorekeeper.txt", "a")
    # Write the total score to the file
    file.write(f"\nThe total score after these 5 rounds you played is: {totalScore}\n")
    file.close()

    file = open("Scorekeeper.txt")
    
    # Ask the user if they want to view the scoreboard
    answer = input("Would you like to view the scoreboard? Answer 'yes' or 'no': ")

    if answer == 'yes' or 'Yes':
        print()
        print(file.read()) # Read the scoreboard from the file

    file.close() 
    
file = open("Scorekeeper.txt", "w")

# Explain the game to the user
print("Welcome to Guess the Number! As two dice are rolled, you must guess the sum of the two numbers rolled!")
print("In this game, you will get 3 guesses to get the right number and have 5 rounds!")
print("You may play again if you wish to!")

name = input("\nEnter your name to start: ")
file.write(f"Scoreboard for: {name}\n") # Write the name of the user to the file

file.close()

main() # Call on the main function to play the game

# Ask the user if they want to play again
choice = input("Do you want to play again? Answer 'yes' or 'no': ").lower()

while choice == 'yes': # Play the game again until the user answers 'no'
    main()
    choice = input("Do you want to play again? Answer 'yes' or 'no': ").lower()

if choice == 'no': # If the user is done playing, say goodbye
    print("Thank you for playing! Bye-bye!")