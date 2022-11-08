# Scissors / paper / stone
turn1 = input("Player 1 turn: ")
turn2 = input("Player 2 turn: ")

if turn1 == turn2:
    # draw
    print("Draw")
else:
    # someone wins
    if turn1 == 'paper':
        if turn2 == 'scissors':
            print("2 wins")
        else:
            print("1 wins")
    elif turn1 == "scissors":
        if turn2 == 'paper':
            print("1 wins")
        else:
            print("2 wins")
    elif turn1 == 'stone':
        if turn2 == 'paper':
            print("2 wins")
        else:
            print("1 wins")