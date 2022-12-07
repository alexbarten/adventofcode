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
            for _ in trail:
                key = ''.join(unpeel)
                fs[key] += int(size)
                unpeel.pop()

    close_fit = fs['/']
    free = 70000000 - close_fit
    needed = 30000000 - free
    for folder in fs:
        if fs[folder] >= needed and fs[folder] < close_fit:
            close_fit = fs[folder]

    print(close_fit)
