with open('2022/day08/day08_1.txt', 'r') as tth:
    x = y = 1
    forestlines = 0
    forestmap = dict()
    for forestline in tth:
        forestline = forestline.rstrip()
        forestlines += 1
        for tree in forestline:
            forestmap[x, y] = tree
            x += 1
        x = 1; y += 1

    visible_trees = 0
    for key, val in forestmap.items():
        if 1 in key:
            visible_trees += 1
        elif len(forestline) in key:
            visible_trees += 1
        else:
            visi_l = visi_u = visi_r = visi_d = True
            x, y = key
            for i in range(1, x):
                if int(forestmap[i, y]) >= int(forestmap[x, y]):
                    visi_l = False
            for i in range(x + 1, len(forestline) + 1):
                if int(forestmap[i, y]) >= int(forestmap[x, y]):
                    visi_r = False
            for i in range(1, y):
                if int(forestmap[x, i]) >= int(forestmap[x, y]):
                    visi_u = False
            for i in range(y + 1, forestlines + 1):
                if int(forestmap[x, i]) >= int(forestmap[x, y]):
                    visi_d = False
            if visi_l or visi_r or visi_u or visi_d:
                visible_trees += 1

    print(visible_trees)
