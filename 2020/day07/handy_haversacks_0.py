def main():
    graph = create_graph('day07/bags_0.txt')
    containers = determine_containers(graph, 'shiny gold bag')
    print(containers)


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
    key = {i for i in graph if graph[i] == bag}
    return key


if __name__ == '__main__':
    main()
