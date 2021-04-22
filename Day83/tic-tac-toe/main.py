# Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
# The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a
# 2-player game, where one person is "X" and the other plays "O".

game_on = True
valid_move = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']

turn = 0

row0 = ["   ", "1", "2", "3"]
row1 = [" A ", " ", " ", " "]
row2 = [" B ", " ", " ", " "]
row3 = [" C ", " ", " ", " "]

def show_board():
    print(row0)
    print(row1)
    print(row2)
    print(row3)

show_board()

while game_on is True:
    # Set marker for X or O turn
    if turn % 2 == 0:
        marker = "X"
    else:
        marker = "O"

    # Ask for player's move
    square = input("Your move: ").upper()
    # Verify the move is open
    if square in valid_move:
        valid_move.remove(square)
        ltr = str(square[0])
        nbr = int(square[1])
        if ltr == "A":
            row1[nbr] = marker
        elif ltr =="B":
            row2[nbr] = marker
        else:
            row3[nbr] = marker

        # Check if the game is won
        if turn >= 4:
            if row1[1] == row1[2] == row1[3]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row2[1] == row2[2] == row2[3]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row3[1] == row3[2] == row3[3]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row1[1] == row2[1] == row3[1]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row1[2] == row2[2] == row3[2]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row1[3] == row2[3] == row3[3]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row1[1] == row2[2] == row3[3]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif row1[3] == row2[2] == row3[1]:
                print(f"Game over, {marker} wins!")
                game_on = False
            elif valid_move == []:
                print("Game over, Draw.")
                game_on = False
    else:
        print("invalid move, try again")
        turn -= 1

    show_board()

    # Next player's turn
    turn += 1



