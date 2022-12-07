def main():
    print(multiply_entries((find_entries_of_sum(2020, 'day01/entries_1.txt'))))


def find_entries_of_sum(sum, entries):
    """find_entries_of_sum

    For a given number and a list of input entries, this function returns
    the two entries from the list that together make up this number.

    Args:
        sum (int): number to be summarized from two entries
        entries (text file): file of entries (one entry per line)

    Returns:
        list: entry 1, entry 2
    """
    entrylist = []
    with open(entries, 'r') as sumentries:
        for entry in sumentries:
            entrylist.append(int(entry))

    for entry in entrylist:
        if (sum - entry) in entrylist:
            return [entry, sum - entry]


def multiply_entries(entrylist):
    return entrylist[0] * entrylist[1]


if __name__ == "__main__":
    main()
