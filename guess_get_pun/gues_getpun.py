import requests
import random


def get_random_joke():
    try:
        response = requests.get('https://punapi.rest/api/pun')
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data['pun']
        else:
            return "No puns today, sorry"
    except Exception as e:
        return f"Error: {e}"


def guess_the_dice_roll():
    user_guess = input("I'll throw the dice, guess what will come up (enter a number from 1 to 6):")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if 1 <= user_guess <= 6:
            dice_roll = random.randint(1, 6)
            print(f"The nuber is: {dice_roll}")
            if user_guess == dice_roll:
                print(f"You guessed it! Here's a joke for you: {get_random_joke()}")
            else:
                print("Unfortunately, you guessed wrong. Try again!")
        else:
            print("The number must be in the range from 1 to 6.")
    else:
        print("Please enter a valid number.")


if __name__ == "__main__":
    guess_the_dice_roll()
