alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
priority = {}
for i in range(1, 53):
    priority[alphabet[i-1]] = i
with open('input.txt') as infile:
    lines = infile.readlines()
    total = 0
    for line in lines:
        line = line.strip()
        part1 = line[:len(line)//2]
        part2 = line[len(line)//2:]
        for letter in part1:
            if letter in part2:
                total += priority[letter]
                break
    print(total)