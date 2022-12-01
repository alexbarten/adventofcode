def main():
    calorielist = compute_calories_per_elf('day01/day01_1.txt')
    highest_set = highest_numbers(calorielist, 3)
    print("Highest number of calories carried by three elves: ",
          sum(highest_set))


def compute_calories_per_elf(calories_per_elf):
    current_calories = 0
    computed_calories = list()
    with open(calories_per_elf, 'r') as ce:
        for entry in ce:
            entry = entry.strip()
            if entry != "":
                current_calories += int(entry)
            else:
                computed_calories.append(current_calories)
                current_calories = 0
        computed_calories.append(current_calories)

    computed_calories.sort(reverse=True)
    return computed_calories


def highest_numbers(calorieset, number):
    return calorieset[:number]


if __name__ == "__main__":
    main()
