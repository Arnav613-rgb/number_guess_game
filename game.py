import random

def number_guessing_game():
    """Builds and runs a command-line number guessing game."""
    
    # 1. Generate a random secret number between 1 and 100
    SECRET_NUMBER = random.randint(1, 100)
    MAX_GUESSES = 7
    guesses_left = MAX_GUESSES
    
    print("-" * 40)
    print("Welcome to the Number Guessing Game!")
    print(f"I have picked a number between 1 and 100.")
    print(f"You have {MAX_GUESSES} guesses to find it.")
    print("-" * 40)

    # 2. Start the guessing loop
    while guesses_left > 0:
        print(f"\nGuesses left: {guesses_left}")
        
        try:
            # 3. Get user input
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            
            # 4. Compare the guess to the secret number
            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess == SECRET_NUMBER:
                print(f"\nCongratulations! You guessed the number {SECRET_NUMBER} correctly!")
                return # End the game function

            elif guess < SECRET_NUMBER:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            guesses_left -= 1

        except ValueError:
            # Handle cases where the user enters text instead of a number
            print("Invalid input. Please enter a whole number.")

    # 5. Handle game over condition
    print("-" * 40)
    print(f"Game Over! You ran out of guesses.")
    print(f"The secret number was {SECRET_NUMBER}.")
    print("-" * 40)

# This line ensures the function runs when you execute the script
if __name__ == "__main__":
    number_guessing_game()
