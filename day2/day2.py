score_key = {
    '[\'A\', \'X\']': 3,
    '[\'A\', \'Y\']': 4,
    '[\'A\', \'Z\']': 8,
    '[\'B\', \'X\']': 1,
    '[\'B\', \'Y\']': 5,
    '[\'B\', \'Z\']': 9,
    '[\'C\', \'X\']': 2,
    '[\'C\', \'Y\']': 6,
    '[\'C\', \'Z\']': 7 
    }

with open('input.txt') as file:
    lines = file.readlines()

total=0
for line in lines:
    rps = line.replace('\n','').split(' ')
    total += score_key[str(rps)]
print(total)