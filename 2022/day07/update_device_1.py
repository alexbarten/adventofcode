with open('2022/day07/day07_1.txt', 'r') as td:
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

    total_size = 0
    for folder in fs:
        if fs[folder] <= 100000:
            total_size += fs[folder]

    print(total_size)
