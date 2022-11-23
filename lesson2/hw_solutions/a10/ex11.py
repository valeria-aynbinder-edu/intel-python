# Generate a random number between 1 and 100 (including 1 and 100).
# Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right.
# (Hint: the following two lines will return you a random number between 1 and 10):
#
# import random
# random_num = random.randint(1, 10)
#
# Keep the game going until the user types “exit”. Keep track of how many guesses the
# user has taken, and when the game ends, print this out.


import random
random_num = random.randint(1, 100)
guess_cnt = 0

while True:
    guess = input("Insert your guess: ")
    if guess == "exit":
        print("Total guess count:", guess_cnt, "Bye-bye!")
        break
    else:
        guess_cnt += 1
        guess = int(guess)
        if guess == random_num:
            print(f"You guessed it! Total guess number: {guess_cnt}")
            break
        elif guess < random_num:
            print("Too small")
        else:
            print("Too big")
