with open('input.txt') as f:
    lines = f.readlines()
elfDict = {}
elfNumber = 1
currentElf = 0
for line in lines:
    if line != '\n':
        currentElf += int(line)
    else:
        elfDict[elfNumber] = currentElf
        elfNumber += 1
        currentElf = 0
values = list(elfDict.values())
values.sort()
print(values[-1] + values[-2] + values[-3])