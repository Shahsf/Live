def welcome(name):
    return (f"Hello {name} and welcome to the World of Games "
            f"here you can find many cool games to play")


def load_game():
    game_options = {'1': 'Memory Game - a sequence of numbers will apper for 1 second and you have to guess it back',
                    '2': 'Guess Game-guess a number and see if you chose like the computer',
                    '3': 'Currency Roulette - try and guess the balue of a random amount of Usd in iLS'}
    game_input = input(
        "Choose a Game to Play- \n 1: Memory Game - a sequence of numbers will apper for 1 second and you have to "
        "guess it back\n 2: Guess Game-guess a number and see if you chose like the computer\n 3: Currency Roulette - "
        "try and guess the value of a random amount of Usd in iLS \n Choose The game Number: ")

    while game_input not in game_options:
        print("You Entered an Invalid Input Please Try again")
        game_input = input(
            "Choose a Game to Play- \n 1: Memory Game - a sequence of numbers will apper for 1 second and you have to "
            "guess it back\n 2: Guess Game-guess a number and see if you chose like the computer\n 3: Currency "
            "Roulette - try and guess the value of a random amount of Usd in iLS \n Choose The game Number: ")

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
