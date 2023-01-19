import random

plays = ["ROCK","PAPER","SCISSORS"]
humanWins = [-2, 1]
humanCount = 0
computerCount = 0

def getValidHumanPlay( low, high ):
    valid = False
    while not valid:
        playerPick = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
        if playerPick >= low and playerPick <= high:
            valid = True
        else:
            valid = False
    return playerPick

def getPlay( human, plays ):
    morePlays = True
    while morePlays:
        humanPlay = getValidHumanPlay(0,2)
        computerPlay = random.randint(0,2)
        print("Human chose: "+ str(plays[humanPlay]))
        print("Computer chose: "+ str(plays[computerPlay]))
        if humanPlay == computerPlay:
            morePlays = True
        else:
            morePlays = False
            return humanPlay, computerPlay

def checkWinner( play, plays, humanCount, computerCount ):
    result = play[0]-play[1]
    if result in humanWins:
        humanCount += 1
        print("Human won with " + plays[play[0]] + " beating " + plays[play[1]])
    else:
        computerCount += 1
        print("Computer won with " + plays[play[1]] + " beating " + plays[play[0]])
        
    return [humanCount, computerCount]

human = input( "Enter your name: ").upper()

keepPlaying = True

while keepPlaying:
    play = getPlay(human, plays)
    winner = checkWinner(play, plays, humanCount, computerCount)
    humanCount, computerCount = winner[0], winner[1]
    if humanCount < 3 and computerCount < 3:
        keepPlaying = True
    else:
        keepPlaying = False
    
    
if humanCount == 3:
    print(human + " wins!")
    print("Human: " + str(humanCount) + "\nComputer: " + str(computerCount))
elif computerCount == 3:
    print("Computer wins!")
    print("Computer: " + str(computerCount) + "\nHuman: " + str(humanCount))
