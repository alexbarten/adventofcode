def main():
    calorielist = compute_calories_per_elf('day01/day01_1.txt')
    highest_set = get_highest_numbers(calorielist, 3)

    print("Highest number of calories carried by three elves: ",
          sum(highest_set))


def compute_calories_per_elf(caloriefile):
    one_elf_cals = 0
    all_elf_cals = list()

    with open(caloriefile, 'r') as ce:
        for entry in ce:
            entry = entry.strip()
            if entry != "":
                one_elf_cals += int(entry)
            else:
                all_elf_cals.append(one_elf_cals)
                one_elf_cals = 0

        all_elf_cals.append(one_elf_cals)

    all_elf_cals.sort(reverse=True)
    return all_elf_cals


def get_highest_numbers(calorielist, number):
    return calorielist[:number]


if __name__ == "__main__":
    main()
