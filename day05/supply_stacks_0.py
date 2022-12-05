def main():
    print(create('day05/day05_0.txt'))


def create(stacks):
    with open(stacks, 'r') as st:
        stacklist = ['', '', '']
        for level in st:
            if level.strip() == '':
                continue
            elif level[1] == '1':
                for i in range(3):
                    stacklist[i] = stacklist[i][::-1].rstrip()
            elif level[0:4] == 'move':
                nr, orig, dest = [int(i) for i in level.split() if i.isdigit()]
                stacklist[dest-1] += stacklist[orig-1][(nr * -1):]
                # stacklist[orig-1] = stacklist[orig-1][:len(stacklist)-nr]
            else:
                stackcounter = 0
                for crate in range(1, len(level), 4):
                    print(level[crate] + str(crate))
                    stacklist[stackcounter] += level[crate]
                    stackcounter += 1

        return stacklist


if __name__ == '__main__':
    main()
