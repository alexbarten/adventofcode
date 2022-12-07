def find_entries_of_sum(sum, entries):
    entrylist = []
    with open(entries, 'r') as sumentries:
        for entry in sumentries:
            entrylist.append(int(entry))

    for entry in entrylist:
        if (2020 - entry) in entrylist:
            return [entry, 2020 - entry]


def multiply_entries(entry1, entry2):
    return entry1 * entry2
