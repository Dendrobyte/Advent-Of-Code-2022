inputFile = open("inputs/Day_X.txt", "r+")
inputData = inputFile.read().split("\n")
inputFile.close()
# del inputData[len(inputData)-1] -- in case of new line
