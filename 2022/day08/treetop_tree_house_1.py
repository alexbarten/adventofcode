with open('2022/day08/day08_0.txt', 'r') as tth:
    x = y = 1
    forestmap = dict()
    for forestline in tth:
        for tree in forestline.rstrip():
            forestmap[x, y] = tree
            x += 1
        x = 1; y += 1

    print(forestmap)
