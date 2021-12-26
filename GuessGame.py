import random


def generate_number(sec_num):
    difficulty = int(input("Please Choose game difficulty from 1 to 5: "))
    if difficulty == 1:
        difficulty = 1
    elif difficulty == 2:
        difficulty = 2
    elif difficulty == 3:
        difficulty = 3
    elif difficulty == 4:
        difficulty = 4
    elif difficulty == 5:
        difficulty = 5
    else:
        print("You Choose difficulty that Doesn't exist Please try again")
        difficulty = int(input("Please Choose game difficulty from 1 to 5: "))

    secret_number = random.randint(1, difficulty + 1)
    sec_num = secret_number


def get_guess_from_user(user_guess):
    player_guess = int(input("Try to Guess The Number between 1 to ur Difficulty:"))
    if 6 >= player_guess and player_guess > 0:
        return
    else:
        print("You Choose Number not in the range")
        player_guess = int(input("Try to Guess The Number between 1 to ur Difficulty:"))
    player_guess = user_guess


def compare_results(sec_num=generate_number(), user_guess=get_guess_from_user()):
    if user_guess == sec_num:
        print("True")
    else:
        print("False")


def play():
    (generate_number(2))
    (get_guess_from_user(2))
    return compare_results()


print(play())

