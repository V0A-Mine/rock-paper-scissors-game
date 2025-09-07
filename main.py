
def is_win(player, opponent):
    return True if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r") else False
    

import random
def play():
    while True:
        rps = ["r", "p", "s"]
        bot = random.choice(rps)
        user = input("Rock, Paper, Scissors (r/p/s): ").lower()
        if user.isalpha():
            if user == bot:
                print(f"\nYour choices are same ({bot.upper()})\n")
                pass
            elif is_win(user, bot) == True:
                print(f"You won ({user.upper()}), The opponent is {bot.upper()}\n")
                exit()
            elif is_win(user, bot) == False:
                print(f"You lost ({user.upper()}), The oponent is {bot.upper()}\n")
                exit()
            else:
                print("\nYou can only input (r, p, s)\n")
                pass
        else:
            print("\nYou can only input (r, p, s)\n")
            pass
    

play()
