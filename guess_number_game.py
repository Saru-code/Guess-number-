import random

def guess_number_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

if __name__ == "__main__":
    guess_number_game()

