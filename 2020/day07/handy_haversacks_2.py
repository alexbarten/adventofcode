def main():
    graph = create_graph('2020/day07/bags_1.txt')
    print(determine_containers(graph, 'shiny gold bag'))


def create_graph(bags):
    with open(bags, 'r') as bg:
        group = dict()
        for line in bg:
            line = line.replace('bags', 'bag')
            line = line.replace('.', '')
            line = ''.join((x for x in line if not x.isdigit()))
            bags = [phrase.strip() for phrase in line.split('contain')]
            group[bags[0]] = [phrase.strip() for phrase in bags[1].split(', ')]

        return group


def determine_containers(graph, bag):
    counter = set()
    bags = [bag]
    bag = bags.pop()
    while True:
        values = [key for key, value in graph.items() if bag in value]
        if len(keys) > 0:
            counter.update(keys)
            bags.extend(keys)
            bag = bags.pop()
        else:
            if len(bags) > 0:
                bag = bags.pop()
            else:
                break
    return len(counter)


if __name__ == '__main__':
    main()
