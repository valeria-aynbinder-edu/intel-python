# Make a continuous two-player Rock-Paper-Scissors game.
# Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game).
# In addition, keep track of the amount of wins / draws for each round,
# and when the user chooses to exit your program,
# print all the statistics of the game - total rounds played, total wins for each player, total draws.
# The rules are:
# Rock beats scissors
# Scissors beat paper
# Paper beats rock


wins1 = 0
wins2 = 0
draws = 0

while True:
    answer = input("Do you want to play a game? (y/n)").lower()
    if answer == 'n':
        print(f"Total rounds played: {wins1 + wins2 + draws},\n"
              f"Total wins for player 1: {wins1},\n"
              f"total wins for player 2: {wins2},\n"
              f"draws: {draws}")
        print("bye-bye")
        exit(0)
    else:
        p1 = input("Player 1 turn (r - rock, s - scissors, p - paper): ")
        p2 = input("Player 2 turn (r - rock, s - scissors, p - paper): ")
        if p1 == p2:
            print("Draw")
            draws += 1
        elif p1 == "s":
            if p2 == 'r':
                print("2 wins")
                wins2 += 1
            else:
                print("1 wins")
                wins1 += 1
        elif p1 == "p":
            if p2 == "s":
                print("2 wins")
                wins2 += 1
            else:
                print("1 wins")
                wins1 += 1
        elif p1 == "r":
            if p2 == "s":
                print("1 wins")
                wins1 += 1
            else:
                print("2 wins")
                wins2 += 1