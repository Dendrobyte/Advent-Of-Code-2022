inputFile = open("inputs/day1.txt", "r+")
inputData = inputFile.read().split("\n")
inputFile.close()

'''Part 1'''
maxCals = -1
currCals = 0
# Literally just add up until I hit new line and save the max
for line in inputData:
    if line != '':
        currCals += int(line)
    else:
        maxCals = currCals if currCals > maxCals else maxCals
        currCals = 0

# print(maxCals)

'''Part 2'''
maxCals = [-3, -2, -1]
currCals = 0
# Same process, iterate over top three maxes
for line in inputData:
    if line != '':
        currCals += int(line)
    else:
        # Order doesn't matter, so just always compare against the min
        currMin = min(maxCals)
        minInd = maxCals.index(currMin)
        maxCals[minInd] = currCals if currCals > currMin else maxCals[minInd]
        currCals = 0

print(sum(maxCals))  # It's nto 197683
