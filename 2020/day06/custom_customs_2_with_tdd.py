def main():
    print(turn_file_into_groups('day06/customs_questions_1.txt'))


def turn_file_into_groups(customs_questions):
    with open(customs_questions, 'r') as cq:
        group = list()
        result = 0
        for row in cq:
            row = row.strip()
            if row != '':
                group.append(row)
            else:
                result += count_answers(group)
                group.clear()

    result += count_answers(group)
    return result


def count_answers(answers):
    group = list()
    for row in answers:
        group.append(set(row))
    result = set.intersection(*group)
    return int(len(result))


if __name__ == "__main__":
    main()
