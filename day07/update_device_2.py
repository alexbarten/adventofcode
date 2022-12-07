with open('day07/day07_1.txt', 'r') as td:
    fs = dict()
    trail = list()

    for cli in td:
        if cli[0:4] == '$ cd':
            _, _, cd = cli.rstrip().split(' ')
            if cd != '..':
                trail.append(cd)
                key = ''.join(trail)
                fs[key] = 0
            else:
                cd = trail.pop()
        elif cli[0:4] in ['$ ls', 'dir ']:
            continue
        else:
            size, _ = cli.rstrip().split(' ')
            unpeel = trail.copy()
            for directory in trail:
                key = ''.join(unpeel)
                fs[key] += int(size)
                unpeel.pop()

    largest_yet = fs['/']
    free = 70000000 - largest_yet
    needed = 30000000 - free
    for folder in fs:
        if fs[folder] >= needed and fs[folder] < largest_yet:
            largest_yet = fs[folder]

    print(largest_yet)
