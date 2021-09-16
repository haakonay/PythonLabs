import random


# generate a board
# place mines randomly on the board
# Calculate for each mine the number of neighboring mines
# Create a mask for the board so players cant see mines

# Step 2
# User provides a coordinate or exits the game
# The script then unmasks the desire coordinate
# if the coordinate is a mine, then the player loses
# unmasking the entire board and printing "you lost!"

# Step 3
# Check if the player has found all the mines after each check
# if this is the case print "you won", and unmask the entire board

def buildBoard():
    sizeX = 3
    sizeY = 3
    bombs = 3
    totalOptions = (sizeX * sizeY) - bombs

    # tempBoard is bigger than the users desired board two avoid indices out of range later
    tempBoard = [[0] * (sizeX + 2) for i in range(sizeY + 2)]
    boardMines = tempBoard
    # Putting bombs in the users desired xy field (not in the actual field)

    for i in range(bombs):
        bombPosX = random.randint(1, sizeX)  # 0-4 (5)
        bombPosY = random.randint(1, sizeY)
        while boardMines[bombPosX][bombPosY] == "*":
            bombPosX = random.randint(1, sizeX)
            bombPosY = random.randint(1, sizeY)
            # Checks if that position already has a bomb, if so, continue the while loop
            if boardMines[bombPosX][bombPosY] == "*":
                continue
        boardMines[bombPosX][bombPosY] = "*"  # Placing bomb

    # Incrementing surrounding fields
    # Still using tempBoard, but reducing the range
    for i in range(1, sizeX + 1):  #
        for j in range(1, sizeY + 1):
            if boardMines[i][j] == "*":
                if boardMines[i + 1][j] != "*": boardMines[i + 1][j] += 1
                if boardMines[i + 1][j - 1] != "*": boardMines[i + 1][j - 1] += 1
                if boardMines[i + 1][j + 1] != "*": boardMines[i + 1][j + 1] += 1
                if boardMines[i][j + 1] != "*": boardMines[i][j + 1] += 1
                if boardMines[i][j - 1] != "*": boardMines[i][j - 1] += 1
                if boardMines[i - 1][j] != "*": boardMines[i - 1][j] += 1
                if boardMines[i - 1][j + 1] != "*": boardMines[i - 1][j + 1] += 1
                if boardMines[i - 1][j - 1] != "*": boardMines[i - 1][j - 1] += 1

        # over -1, over, over +1, høyre, venstre, under -1, under, under +1

    maskedBoard = [["?"] * sizeX for i in range(sizeY)]
    # print(*maskedBoard, sep="\n")
    # print(*boardMines, sep="\n")

    board = [[0] * sizeX for i in range(sizeY)]  # Actual size of board
    # Filling up board

    for i in range(0, sizeX):
        for j in range(0, sizeY):
            board[i][j] = boardMines[i + 1][j + 1]

    # print(*board, sep="\n")

    return maskedBoard, board, totalOptions, sizeX, sizeY
def choice(xCoordinateMax, yCoordinateMax):
    coordinate = True
    while coordinate:
        xcoordinate = input(f"Write in x coordinate between (0-{xCoordinateMax-1}) or \"exit\" ")
        if xcoordinate == "exit":
            return 666, 666
        ycoordinate = input(f"Write in y coordinate between (0-{yCoordinateMax-1}) ")
        if int(xcoordinate) not in range(0, xCoordinateMax) or int(ycoordinate) not in range(0, yCoordinateMax):
            print("Number not in range. Try again or \"exit\": ")
        else:
            return int(xcoordinate),  int(ycoordinate)



maskedBoard, board, totalOptions, sizeX, sizeY = buildBoard()

print(*board, sep="\n")
print(*maskedBoard, sep="\n")


# User input
# Skriv inn x koordinat, skriv inn y koordinat. Skriv exit for å komme deg ut
# if valg = int mellom () elif valg = exit

# +1 etter hvert input


print(sizeX)
vx, vy = choice(sizeX, sizeY)
totalAttempts = 1

while board[vx][vy] != "*":
    maskedBoard[vx][vy] = board[vx][vy]
    print(*maskedBoard, sep="\n")
    if totalAttempts == totalOptions:
        print("Congrats you won!")
        break
    vx, vy = choice(sizeX, sizeY)
    if vx == 666:
        break
    totalAttempts += 1

if board[vx][vy] == '*':
    print("Bomb exploded. Game over ")
else:
    print("Exited game..")






