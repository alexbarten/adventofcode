with open('2022/day10/day10_1.txt', 'r') as crt:
    values = list()
    value = 1
    for signal in crt:
        if signal.rstrip() == 'noop':
            values.append(value)
        else:
            _, new_value = signal.rstrip().split(' ')
            values.extend((value, value))
            value += int(new_value)

    checkline = 20
    total = 0
    for i in range(6):
        total += values[checkline - 1] * checkline
        checkline += 40

    print(total)
