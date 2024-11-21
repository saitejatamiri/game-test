import random

def guess_number():
    # Set the range for the random number
    lower = 1
    upper = 100
    number_to_guess = random.randint(lower, upper)

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower} and {upper}.")

    attempts = 0
    while True:
        # Ask the user to input their guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()
