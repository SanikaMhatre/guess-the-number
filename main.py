
from random import randint
from art import logo

def level(difficulty):
    if difficulty == "easy":
        attempts = 10
        print(f"You have {attempts} attempts to guess the number")
    elif difficulty == "hard":
        attempts = 5
        print(f"You have {attempts} attempts to guess the number")
    else:
        print("Enter correct difficulty level")
    return attempts

def guess(attempts, choosed):
    guessed_number = int(input("Make a guess: "))
    return guessed_number

def selected_number():
    # numbers = []
    # for i in range(1, 101):
    #     numbers.append(i)

    # number = random.choice(numbers)
    number = randint(1,100) #1 and 100 are both included
    return number

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    choosed = 0
    choosed += selected_number()
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    remaining_attempts = level(difficulty)
    print(remaining_attempts)
    game_over = False
    while not game_over:
      new_guess = guess(remaining_attempts, choosed)
      remaining_attempts -= 1
      if remaining_attempts == 0:
        print("You lose. No attempts left")
        game_over = True
      elif new_guess == choosed:
        print(f"You got it! The answer was {choosed}")
        game_over = True
      elif new_guess < choosed:
        print("Too low.")
        print(f"You have {remaining_attempts} attempts remaining to guess the number")
      elif new_guess > choosed:
        print("Too high.")
        print(f"You have {remaining_attempts} attempts remaining to guess the number")
              
play_game()
