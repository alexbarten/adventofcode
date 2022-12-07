def main():
    print(calculate_seat('day05/boardingpasses_1.txt'))


def calculate_seat(boardingpasses):
    with open(boardingpasses, 'r') as bp:
        places = set()
        for boardingpass in bp:
            boardingpass = boardingpass.replace('F', '0')
            boardingpass = boardingpass.replace('B', '1')
            boardingpass = boardingpass.replace('R', '1')
            boardingpass = boardingpass.replace('L', '0')

            row = int(boardingpass[0:7], 2)
            column = int(boardingpass[7:], 2)
            places.add(row * 8 + column)

            seat_id = set(range(min(places), max(places))) - places

    return seat_id


if __name__ == "__main__":
    main()
