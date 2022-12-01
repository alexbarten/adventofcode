def main():
    print("Highest calories per elf: ",
          compute_calories_per_elf('day01/day01_1.txt'))


def compute_calories_per_elf(caloriefile):
    max_cals = 0
    one_elf_cals = 0
    with open(caloriefile, 'r') as ce:
        for entry in ce:
            entry = entry.rstrip()
            if entry != "":
                one_elf_cals += int(entry)
            else:
                if one_elf_cals > max_cals:
                    max_cals = one_elf_cals
                one_elf_cals = 0

    return max_cals


if __name__ == "__main__":
    main()
