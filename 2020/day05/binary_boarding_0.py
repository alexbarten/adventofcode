def main():
    print(calculate_seat('day05/boardingpasses_0.txt'))


def calculate_seat(boardingpasses):
    with open(boardingpasses, 'r') as bp:
        high_seat_id = 0

        for boardingpass in bp:
            boardingpass = boardingpass.replace('F', '0')
            boardingpass = boardingpass.replace('B', '1')
            boardingpass = boardingpass.replace('R', '1')
            boardingpass = boardingpass.replace('L', '0')

            row = int(boardingpass[0:7], 2)
            column = int(boardingpass[7:], 2)
            seat_id = row * 8 + column
            if seat_id > high_seat_id:
                high_seat_id = seat_id

    return high_seat_id


if __name__ == "__main__":
    main()
