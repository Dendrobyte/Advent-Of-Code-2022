inputFile = open("inputs/day2.txt", "r+")
inputData = inputFile.read().split("\n")
inputFile.close()
# del inputData[len(inputData)-1] -- in case of new line

# 1 is rock, 2 is paper, 3 is scissors
gameVals = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

# list of pairs such that player wins
wins = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
# list of draws
draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]

'''Part 1'''
totalPoints = 0
for line in inputData:
    vals = line.split(" ")
    pair = (vals[0], vals[1])
    if pair in wins:  # we have a win
        pPoints = gameVals[vals[1]] + 6
    elif pair in draws:
        pPoints = gameVals[vals[1]] + 3
    else:
        pPoints = gameVals[vals[1]] + 0
    totalPoints += pPoints
# print(totalPoints)

'''Part 2'''
winMap = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}
drawMap = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}
lossMap = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
totalPoints = 0
for line in inputData:
    vals = line.split(" ")
    pair = (vals[0], vals[1])
    if vals[1] == 'X':  # you lose
        yourChoice = lossMap.get(vals[0])
        pPoints = gameVals.get(yourChoice) + 0
    elif vals[1] == 'Y':  # draw
        yourChoice = drawMap.get(vals[0])
        pPoints = gameVals.get(yourChoice) + 3
    else:  # loss
        yourChoice = winMap.get(vals[0])
        pPoints = gameVals.get(yourChoice) + 6
    totalPoints += pPoints
print(totalPoints)
