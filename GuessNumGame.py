#Importing the random module
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum attempts allowed
max_attempts = 3

# Function to display a welcome message          
def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")

# Function for recursive guessing
def guess_recursive(attempts_left):
    # Get user input
    guess = int(input("\nGuess the number (Betrween 1 to 10): "))

    # Check ift he guess is correct
    if guess == secret_number:
        print("Congratulations! You have guessed the correct number.")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left > 1:
            # MAke another recursuve call for thr guess
            guess_recursive(attempts_left-1)
        else:
            print(f"\nSorry, you could not guess the number. The correct number was {secret_number}.")
            
        #Calling function
welcome_message()
guess_recursive(max_attempts)

#Using id() to get memory access
print(f"Memory address of Secret Number {secret_number} is: {id(secret_number)}")