alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
priority = {}
for i in range(1, 53):
    priority[alphabet[i-1]] = i
with open('input.txt') as infile:
    #three elves have one of the same item
    lines = infile.readlines()
    #group every three lines together
    lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
    total = 0
    for line in lines:
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        line[2] = line[2].strip()
        for letter in line[0]:
            if letter in line[1] and letter in line[2]:
                total += priority[letter]
                break
    print(total)
