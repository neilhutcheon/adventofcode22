with open('input.txt') as f:
    line = f.readlines()
    line = [line.strip() for line in line]
    line = line[0]
    found_letters = []
    for index in range(0, len(line)):
        if len(found_letters) < 14: #for part 1 change 14 to 4
            found_letters.append(line[index])
        if len(found_letters) == 14: #for part 1 change 14 to 4
            if len(found_letters) == len(set(found_letters)):
                print(found_letters, index)
                break
            else:
                tmp = found_letters
                found_letters = tmp[1:]
                found_letters.append(line[index])