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

    visible_area = 0
    for key, val in forestmap.items():
        x, y = key
        visi_l = x - 1
        visi_r = len(forestline) - x
        visi_u = y - 1
        visi_d = forestlines - y

        for i in range(x - 1, 0, -1):
            if int(forestmap[i, y]) >= int(forestmap[x, y]):
                visi_l = x - i
                break
        for i in range(x + 1, len(forestline) + 1):
            if int(forestmap[i, y]) >= int(forestmap[x, y]):
                visi_r = i - x
                break
        for i in range(y - 1, 0, -1):
            if int(forestmap[x, i]) >= int(forestmap[x, y]):
                visi_u = y - i
                break
        for i in range(y + 1, forestlines + 1):
            if int(forestmap[x, i]) >= int(forestmap[x, y]):
                visi_d = i - y
                break

        view = visi_l * visi_r * visi_u * visi_d
        if view > visible_area:
            visible_area = view

    print(visible_area)
