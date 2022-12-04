with open('input.txt') as infile:
    lines = infile.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        line = line.split(',')
        line[0] = line[0].split('-')
        line[1] = line[1].split('-')
        # PART 1
        # if int(line[0][0]) >= int(line[1][0]) and int(line[0][1]) <= int(line[1][1]):
        #     print(line)
        #     count += 1
        # elif int(line[1][0]) >= int(line[0][0]) and int(line[1][1]) <= int(line[0][1]):
        #     print(line)
        #     count += 1

        #PART 2 15-37,17-53
        if int(line[0][0]) <= int(line[1][0]) <= int(line[0][1]):
            count += 1
        elif int(line[1][0]) <= int(line[0][0]) <= int(line[1][1]):
            count += 1
    print(count)