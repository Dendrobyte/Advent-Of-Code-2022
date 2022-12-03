inputFile = open("inputs/day3.txt", "r+")
inputData = inputFile.read().split("\n")
inputFile.close()
# del inputData[len(inputData)-1] -- in case of new line

'''Part 1'''
# So pretty much take each line, split in half, find set union
upperOffset = 38  # 'A' has ascii of 65, thus 65-38 = 27
lowerOffset = 96  # 'a' has ascii value of 97, so 97-96 = 1
priorityCount = 0
for line in inputData:
    half = int(len(line) / 2)
    firstHalf = set(line[0:half])
    secondHalf = set(line[half::])
    sim = firstHalf.intersection(secondHalf)
    char = sim.pop()
    priorityCount += ord(char) - \
        upperOffset if char.isupper() else ord(char) - lowerOffset

# print(priorityCount)

'''Part 2'''
n = 3
currGroup = []
priorityCount = 0
for i, line in enumerate(inputData):
    if i % n == 0:
        currGroup = [set(line)]
    else:
        currGroup.append(set(line))
    if len(currGroup) == 3:
        # now we have a list of all three lines for the groups, and we'll just find the intersection of all of them
        badge = currGroup[0].intersection(currGroup[1], currGroup[2]).pop()
        priorityCount += ord(badge) - \
            upperOffset if badge.isupper() else ord(badge) - lowerOffset
print(priorityCount)
