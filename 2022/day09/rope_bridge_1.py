with open('2022/day09/day09_1.txt', 'r') as rb:
    head = [0, 0]
    tail = [0, 0]
    tailmoves = set()
    EOF = False
    while not EOF:
        x_dist = abs(head[0] - tail[0])
        y_dist = abs(head[1] - tail[1])

        if x_dist > 1:
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
            if y_dist > 0:
                if head[1] < tail[1]:
                    tail[1] -= 1
                else:
                    tail[1] += 1
        elif y_dist > 1:
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1
            if x_dist > 0:
                if head[0] < tail[0]:
                    tail[0] -= 1
                else:
                    tail[0] += 1
        else:
            move = rb.readline()
            if move:
                direction, distance = move.rstrip().split(' ')
                match direction:
                    case 'L':
                        head[0] -= int(distance)
                    case 'R':
                        head[0] += int(distance)
                    case 'U':
                        head[1] -= int(distance)
                    case 'D':
                        head[1] += int(distance)
            else:
                EOF = True
        tailmoves.add(tuple(tail))
    print(len(tailmoves))
