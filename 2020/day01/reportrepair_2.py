def main():
    print(multiply_entries((find_entries_of_sum(2020, 'day01/entries_1.txt'))))


def find_entries_of_sum(sum, entries):
    """find_entries_of_sum

    For a given number and a list of input entries, this function returns
    the three entries from the list that together make up this number.

    Args:
        sum (int): number to be summarized from three entries
        entries (text file): file of entries (one entry per line)

    Returns:
        list: entry 1, entry 2, entry 3
    """
    entrylist = []
    with open(entries, 'r') as sumentries:
        for entry in sumentries:
            entrylist.append(int(entry))

    entrylist2 = entrylist

    for entry in entrylist:
        sum_1 = sum - entry
        for entry2 in entrylist2:
            if (sum_1 - entry2) in entrylist2:
                return [entry, entry2, sum_1 - entry2]


def multiply_entries(entrylist):
    return entrylist[0] * entrylist[1] * entrylist[2]


if __name__ == "__main__":
    main()
