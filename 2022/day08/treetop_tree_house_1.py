with open('2022/day08/day08_0.txt', 'r') as tth:
    x = y = 1
    forestmap = dict()
    for forestline in tth:
        for tree in forestline.rstrip():
            forestmap[x, y] = tree
            x += 1
        x = 1; y += 1

    visible_trees = 0
    for key, val in forestmap.items():
        if 1 in key:
            print(key)
            visible_trees += 1
        elif len(forestline) in key:
            print(key)
            visible_trees += 1
        else:
            x, y = key
            surrounding = set()
            # print(x, y)

            surrounding.add(int(forestmap[x-1, y]))
            surrounding.add(int(forestmap[x+1, y]))
            surrounding.add(int(forestmap[x, y-1]))
            surrounding.add(int(forestmap[x, y+1]))
            print(forestmap[x, y], surrounding)
            if int(forestmap[x, y]) > max(surrounding):
                print("bigger")
