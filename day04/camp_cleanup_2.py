import re


def main():
    print(match("day04/day04_1.txt"))


def match(ranges):
    with open(ranges, 'r') as rg:
        range_in_range = 0

        for pair in rg:
            rg1l, rg1h, rg2l, rg2h = re.split(r'[-,]', pair.rstrip())
            rg1 = set(range(int(rg1l), int(rg1h)+1))
            rg2 = set(range(int(rg2l), int(rg2h)+1))

            if rg1.intersection(rg2):
                range_in_range += 1

        return range_in_range


if __name__ == "__main__":
    main()
