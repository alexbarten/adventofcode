def main():
    print("Highest calories per elf: ",
          compute_calories_per_elf('2022/day01/day01_0.txt'))


def compute_calories_per_elf(calories_per_elf):
    highest_calories = 0
    current_calories = 0
    with open(calories_per_elf, 'r') as ce:
        for entry in ce:
            entry = entry.strip()
            if entry != "":
                current_calories += int(entry)
            else:
                if current_calories > highest_calories:
                    highest_calories = current_calories
                current_calories = 0

    return highest_calories


if __name__ == "__main__":
    main()
