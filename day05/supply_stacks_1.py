def main():
    print(process('day05/day05_1.txt'))


def process(stackinput):
    with open(stackinput, 'r') as st:
        stacks = [''] * 9
        for level in st:
            if level.strip() == '':
                continue
            elif level[1] == '1':
                for i in range(len(stacks)):
                    stacks[i] = stacks[i][::-1].rstrip()
            elif level[0:4] == 'move':
                nr, orig, dest = [int(i) for i in level.split() if i.isdigit()]
                stacks[dest-1] += stacks[orig-1][:(-nr - 1):-1]
                stacks[orig-1] = stacks[orig-1][:len(stacks[orig-1])-nr]
            else:
                stackcounter = 0
                for crate in range(1, len(level), 4):
                    stacks[stackcounter] += level[crate]
                    stackcounter += 1

        lastchars = ''
        for i in range(len(stacks)):
            lastchars += str(stacks[i][-1:])

        return lastchars


if __name__ == '__main__':
    main()
