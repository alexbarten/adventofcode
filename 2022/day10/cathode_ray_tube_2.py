def main():
    process_clockcycles('2022/day10/day10_1.txt')


def plot_pixel(pixel, position, screen):
    # TODO: This should become a Class, to prevent returning the input to the
    # caller.
    if pixel == position or pixel == position - 1 or pixel == position + 1:
        screen += '#'
    else:
        screen += ' '

    pixel += 1
    if pixel > 39:
        pixel = 0

    return pixel, screen


def process_clockcycles(cycles):
    pixel = 0
    screen = ''

    with open(cycles, 'r') as crt:
        values = list()
        value = 1
        for signal in crt:
            if signal.rstrip() == 'noop':
                values.append(value)
                pixel, screen = plot_pixel(pixel, value, screen)
            else:
                _, new_value = signal.rstrip().split(' ')
                values.append(value)
                pixel, screen = plot_pixel(pixel, value, screen)
                values.append(value)
                pixel, screen = plot_pixel(pixel, value, screen)
                value += int(new_value)

    for i in range(0, len(screen), 40):
        print(screen[i: i + 40])


if __name__ == "__main__":
    main()
