import sys

valuesDict = dict()
twos = 0
threes = 0
lines = []

for line in sys.stdin:
    lines.append(line)
    wordDict = dict()
    for char in line:
        if char in wordDict:
            wordDict[char] += 1
        else:
            wordDict[char] = 1
    if 2 in wordDict.values():
        twos += 1
    if 3 in wordDict.values():
        threes += 1
print("Check Sum: ", twos*threes)

for line in lines:
    for line2 in lines:
        if line == line2:
            continue
        off = 0
        incorrectChar = 0
        for i in range(len(line)):
            if line[i] != line2[i]:
                off += 1
                incorrectChar = i
            if off > 1:
                break
        if off == 1:
            print("Correct Box: ", line[0:incorrectChar] + line[incorrectChar+1:])
            sys.exit(0)
