def main():
    print(prioritise("2022/day03/day03_1.txt"))


def prioritise(rucksacks):
    with open(rucksacks, 'r') as rs:
        common_items = list()
        items_sum = 0

        for rucksack in rs:
            rucksack = rucksack.rstrip()
            comp1 = set(rucksack[0:int(len(rucksack)/2)])
            comp2 = set(rucksack[int(len(rucksack)/2):])
            common_items.append(comp1.intersection(comp2))

        for item in common_items:
            itemvalue = ord("".join(item))
            if itemvalue > 90:
                items_sum += itemvalue - 96
            else:
                items_sum += itemvalue - 38

        return items_sum


if __name__ == "__main__":
    main()
