with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    containers = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
    initial_built = False
    level = 0
    for line in lines:
        if line != '' and not initial_built:
            #I rearanged the input so it was easier to parse :)
            containers['1'].append(line[2])
            containers['2'].append(line[6])
            containers['3'].append(line[10])
            containers['4'].append(line[14])
            containers['5'].append(line[18])
            containers['6'].append(line[22])
            containers['7'].append(line[26])
            containers['8'].append(line[30])
            containers['9'].append(line[34])
            #for each key in containers remove any elements in the list that are ' '
            for key in containers:
                containers[key] = [x for x in containers[key] if x != ' ']
            level += 1
        if line == '':
            initial_built = True
        if line != '' and initial_built:
            line = line.split(' ')
            num_to_move = int(line[1])
            from_pile = int(line[3])
            to_pile = int(line[5])
            # PART 1
            for i in range(num_to_move):
                containers[str(to_pile)].append(containers[str(from_pile)].pop())

            # PART 2
            # moving = containers[str(from_pile)][-num_to_move:]
            # containers[str(from_pile)] = containers[str(from_pile)][:-num_to_move]
            # containers[str(to_pile)] = containers[str(to_pile)] + moving
    print(containers)