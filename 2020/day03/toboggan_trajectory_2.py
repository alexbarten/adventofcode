def main():
    coordinates = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mult_trees = 1
    for coord in coordinates:
        trees = count_trees('day03/map_1.txt', coord[0], coord[1])
        mult_trees = mult_trees * trees

    print("Multiplied trees: ", mult_trees)


def count_trees(map, x_offset, y_offset):
    map_list = []
    with open(map, 'r') as maplines:
        for mapline in maplines:
            map_list.append(mapline)

    pos_row = 0
    pos_line = 0
    trees_count = 0
    rows = len(map_list[0]) - 1  # We have to deduct the CRLF too.
    for mapline in map_list:
        pos_row += x_offset
        if pos_row > (rows - 1):
            pos_row -= rows

        pos_line += y_offset
        if pos_line >= len(map_list):
            return trees_count

        if map_list[pos_line][pos_row] == '#':
            trees_count += 1


if __name__ == "__main__":
    main()
