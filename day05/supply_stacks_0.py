def main():
    print(create('day05/day05_0.txt'))


def create(stacks):
    with open(stacks, 'r') as st:
        stacklist = ['', '', '']
        for level in st:
            if level.strip() == '':
                continue
            elif level[1] == '1':
                for i in range(len(stacklist)):
                    stacklist[i] = stacklist[i][::-1].rstrip()
                print(stacklist)
            elif level[0:4] == 'move':
                # print('before: ' + str(stacklist))
                nr, orig, dest = [int(i) for i in level.split() if i.isdigit()]
                stacklist[dest-1] += stacklist[orig-1][:(nr * -1 - 1):-1]
                if nr < len(stacklist[orig-1]):
                    # stacklist[orig-1] = stacklist[orig-1][:len(stacklist)-nr]
                    stacklist[orig-1] = stacklist[orig-1].rstrip(stacklist[orig-1][-nr])
                else:
                    stacklist[orig-1] = ''
                # print('after: ' + str(stacklist))
            else:
                stackcounter = 0
                for crate in range(1, len(level), 4):
                    stacklist[stackcounter] += level[crate]
                    stackcounter += 1

        return stacklist


if __name__ == '__main__':
    main()
