def main():
    print('Number of trees:', count_trees_on_trajectory('day03/map_0.txt'))


def count_trees_on_trajectory(map):
    map_list = []
    with open(map, 'r') as maplines:
        for mapline in maplines:
            map_list.append(mapline)

    pos_row = 0
    pos_line = 0
    trees_count = 0
    for mapline in map_list:
        pos_row += 3
        if pos_row > 10:
            pos_row -= 11

        pos_line += 1
        if pos_line == 11:
            return trees_count

        if map_list[pos_line][pos_row] == '#':
            trees_count += 1


if __name__ == "__main__":
    main()
