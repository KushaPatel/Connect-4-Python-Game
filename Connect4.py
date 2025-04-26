import random

# FOR GAME INTRO
print("-----------------------")
print("Welcome to Connect Four")
print("-----------------------")
print()
print("...Some Game Rule...")
print("\nGive your Choice place as \n  1st should be Alphbet. \n  2nd should be Numbers.")
print("\nLike : A3")
print()
print()
print("<<< Game between : You ( 🔵 ) vs Computer ( 🔴 ) >>>")
print()

# FOR MAKING GAMEBOARD
possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

# GAME LAYOUT
def printGameBoard():
  print("\n      A     B     C     D     E     F     G  ")
  for x in range(rows):
    print("\n   |-----|-----|-----|-----|-----|-----|-----|")
    print(x, " |", end="")
    for y in range(cols):
      if(gameBoard[x][y] == "🔵"):
        print("", gameBoard[x][y], end="  |")
      elif(gameBoard[x][y] == "🔴"):
        print("", gameBoard[x][y], end="  |")
      else:
        print(" ", gameBoard[x][y], end="   |")
  print("\n   |-----|-----|-----|-----|-----|-----|-----|")

#FOR GETTING PALCE OF YOUR SIGN
def modifyArray(choosespace, turn):
  gameBoard[choosespace[0]][choosespace[1]] = turn

def checkForWinner(chip):
  # CHECK HORIZONTAL SPACES
  for y in range(rows):
    for x in range(cols - 3):
      if gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip:
        print("\n<<<<Game over>>>>")
        print("   "+chip,  " Wins!")
        print("--Thank you for playing--")
        return True

  # CHECK VERTICAL SPACES
  for x in range(rows):
    for y in range(cols - 3):
      if gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip:
        print("\n<<<<Game over>>>>")
        print("   "+chip,  " Wins!")
        print("--Thank you for playing--")
        return True

  # CHECK UPPER RIGHT TO BOTTOM LEFT DIAGONAL SPACES
  for x in range(rows - 3):
    for y in range(3, cols):
      if gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip:
        print("\n<<<<Game over>>>>")
        print("   "+chip,  " Wins!")
        print("--Thank you for playing--")
        return True

  # CHECK UPPER LEFT TO BOTTOM RIGHT DIAGONAL SPACES
  for x in range(rows - 3):
    for y in range(cols - 3):
      if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
        print("\n<<<<Game over>>>>")
        print("   "+chip,  " Wins!")
        print("--Thank you for playing--")
        return True
  return False

# FOR COMPAIR ALPHABET WITH NUMBERS
def compAlpha(inputString):
  number = [None] * 2
  if(inputString[0] == "A" or inputString[0] == "a"):
    number[1] = 0
  elif(inputString[0] == "B" or inputString[0] == "b"):
    number[1] = 1
  elif(inputString[0] == "C" or inputString[0] == "c"):
    number[1] = 2
  elif(inputString[0] == "D" or inputString[0] == "d"):
    number[1] = 3
  elif(inputString[0] == "E" or inputString[0] == "e"):
    number[1] = 4
  elif(inputString[0] == "F" or inputString[0] == "f"):
    number[1] = 5
  elif(inputString[0] == "G" or inputString[0] == "g"):
    number[1] = 6
  else:
    print("Invalid")
  number[0] = int(inputString[1])
  return number

# CHECK SPACE AVILABLE OR NOT
def isSpaceAvailable(indexnumber):
  if(gameBoard[indexnumber[0]][indexnumber[1]] == '🔴'):
    return False
  elif(gameBoard[indexnumber[0]][indexnumber[1]] == '🔵'):
    return False
  else:
    return True

def properPlaceForChip(indexnumber):
  # CLACULATE SPACE BELOW
  spaceBelow = [None] * 2
  spaceBelow[0] = indexnumber[0] + 1
  spaceBelow[1] = indexnumber[1]
  # IS THE NUMBER AT GROUND LEVEL
  if(spaceBelow[0] == 6):
    return True
  # CHECK IF THERE IS A TOKEN BELOW
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False

#FINAL GAME 
turnCounter = 0
while True:
  if(turnCounter % 2 == 0):
    printGameBoard()
    while True:
      choosespace = input("\nChoose a space: ")
      number = compAlpha(choosespace)
      try:
        # CHECK IF THE SPACE AVAILABLE
        if(isSpaceAvailable(number) and properPlaceForChip(number)):
          modifyArray(number, '🔵')
          break
        else:
          print("Not a valid number.")
      except:
        print("Please, choose appropriate space.")
    winner = checkForWinner('🔵')
    turnCounter += 1

  # FOR COMPUTER TURN
  else:
    while True:
      cpuChoice = [random.choice(possibleLetters), random.randint(0,5)]
      cpunumber = compAlpha(cpuChoice)
      if(isSpaceAvailable(cpunumber) and properPlaceForChip(cpunumber)):
        modifyArray(cpunumber, '🔴')
        break
    turnCounter += 1
    winner = checkForWinner('🔴')

  if(winner):
    print()
    print()
    print("<---Winning game Board--->")
    printGameBoard()
    break