def getFullPath(current_dirs):
    return [''.join(current_dirs[:x+1]) for x in range(len(current_dirs))]

with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    dir_sizes = {}
    current_dirs = []
    for line in lines:
        command = line.split()
        if command[0] == "$":
            command = command[1:]
        if command[0] == "cd":
            if command[1] == "..":
                current_dirs.pop()
            else:
                current_dirs.append(command[1])
        if line.split(' ')[0].isdigit():
            folder = getFullPath(current_dirs)
            for f in folder:
                if f in dir_sizes:
                    dir_sizes[f] += int(line.split(' ')[0])
                else:
                    dir_sizes[f] = int(line.split(' ')[0])

    #create a list of the values in the dir_sizes dictionary
    values = list(dir_sizes.values())
    print(values)
    
    #PART 1
    # total = 0
    # for value in values:
    #     if value <= 100000:
    #         total += value
    # print(total)
    
    #PART 2
    print(dir_sizes['/'])
    free_space = 70000000 - dir_sizes['/']
    needed_space = 30000000 - free_space
    smallest_to_fill = 0
    for key in dir_sizes.keys():
        if dir_sizes[key] > needed_space:
            if smallest_to_fill == 0:
                smallest_to_fill = dir_sizes[key]
            elif dir_sizes[key] < smallest_to_fill:
                smallest_to_fill = dir_sizes[key]
    print(smallest_to_fill)


