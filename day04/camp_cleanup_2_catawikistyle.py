import re

with open("day04/day04_1.txt", 'r') as rg:
    r = 0

    for i in rg:
        r1l, r1h, r2l, r2h = re.split(r'[-,]', i.rstrip())
        r1 = set(range(int(r1l), int(r1h)+1))
        r2 = set(range(int(r2l), int(r2h)+1))

        if r1.intersection(r2):
            r += 1

    print(r)
