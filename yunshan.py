import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Enter your guess (or type 'exit' to quit): ")

        if guess.lower() == 'exit':
            print(f"The number was {number_to_guess}. Thanks for playing!")
            break

        try:
            guess = int(guess)
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

guessing_game()
