import numpy as np
import pandas as pd
import sklearn
import csv
import sys


from sklearn.tree import DecisionTreeClassifier

gameRun = True
rock = 0
paper = 1
scissors = 2
#need to have the algorithm try to predict the players next move and then according to that we choose what beats it


playersMove = pd.read_csv("human_move_history.csv")
botsMove = pd.read_csv("bots_move_history.csv")
playerRound = 1
botRound = 1

model = DecisionTreeClassifier()
human_history = [-1]
bot_history = [-1]
playerRound = 1
botRound = 1
nextMove = 2
gameRound = 0
botsGuess = "nun"
playerWins = 0
botWins = 0
botsGuess2 = 0
while gameRound<9:
    

    Brain = pd.concat([playersMove.iloc[:,0:playerRound],botsMove.iloc[:,0:botRound]],axis = 1)
    playersNextMove = playersMove[f"move{str(nextMove)}"]
    
    model.fit(Brain,playersNextMove)
    

    test = [human_history + bot_history]
    prediction = model.predict(test)
    
    playerRound += 1
    botRound += 1
    nextMove += 1
    playerTurn = input("Rock Paper or Scissors?").lower()
    pt = playerTurn
    if playerTurn == "rock":
        playerTurn = rock
        #0
    elif playerTurn == "paper":
        playerTurn = paper
        #1
    elif playerTurn == "scissors":
        playerTurn = scissors
        #2
    else:
        print("error")
        gameRun = False
        break
    if prediction[0] == rock:
        botsGuess = "paper"
        botsGuess2 = 1
    elif prediction[0] == paper:
        botsGuess = "scissors"
        botsGuess2 = 2
    elif prediction[0] == scissors:
        botsGuess = "rock"
        botsGuess2 = 0

    human_history.append(playerTurn)
    bot_history.append(botsGuess2)
    
    print("your move was: ",pt)
    print("the bots move was: ",botsGuess)
    if (playerTurn == rock) and (botsGuess == "rock"):
        print("tie")
    elif (playerTurn == rock) and (botsGuess == "paper"):
        print("bot wins")
        botWins += 1
    elif (playerTurn == rock) and (botsGuess == "scissors"):
        print("player wins")
        playerWins += 1
    elif (playerTurn == paper) and (botsGuess == "rock"):
        print("player wins")
        playerWins += 1
    elif (playerTurn == paper) and (botsGuess == "paper"):
        print("tie")
    elif (playerTurn == paper) and (botsGuess == "scissors"):
        print("bot wins")
        botWins += 1
    elif (playerTurn == scissors) and (botsGuess == "rock"):
        print("bot wins")
        botWins += 1
    elif (playerTurn == scissors) and (botsGuess == "paper"):
        print("player wins")
        playerWins += 1
    elif (playerTurn == scissors) and (botsGuess == "scissors"):
        print("bot wins")
        botWins += 1
    


    gameRound += 1
if gameRun == False:
    sys.exit(0)
print("human wins: ", playerWins)
print("bot wins: ", botWins)
if playerWins > botWins:
    print("player wins the game")
elif botWins > playerWins:
    print("bot wins the game")
else:
    print("probably a tie")

new_row_human = pd.DataFrame([human_history],columns=["move1","move2","move3","move4","move5","move6","move7","move8","move9","move10"])
new_row_human.to_csv("human_move_history.csv",mode="a",header=False,index=False)
new_row_bot = pd.DataFrame([bot_history],columns=["move1","move2","move3","move4","move5","move6","move7","move8","move9","move10"])
new_row_bot.to_csv("bots_move_history.csv",mode="a",header=False,index=False)
humanData = pd.read_csv("human_move_history.csv")
botData = pd.read_csv("bots_move_history.csv")
#print(humanData)
#print(botData)
