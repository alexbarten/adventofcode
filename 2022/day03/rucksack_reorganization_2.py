def main():
    print(prioritise("2022/day03/day03_1.txt"))


def prioritise(rucksacks):
    with open(rucksacks, 'r') as rs:
        group = list()
        common_items = list()
        items_sum = 0
        eof = False
        rucksack = rs.readline().rstrip()

        while not eof:
            for i in range(3):
                group.append(set(rucksack))

                if i == 2:
                    common_items.append(set.intersection(*group))
                    group = list()
                    i = 0

                rucksack = rs.readline().rstrip()
                if rucksack == "":
                    eof = True

        for item in common_items:
            itemvalue = ord("".join(item))
            if itemvalue > 90:
                items_sum += itemvalue - 96
            else:
                items_sum += itemvalue - 38

        return items_sum


if __name__ == "__main__":
    main()
