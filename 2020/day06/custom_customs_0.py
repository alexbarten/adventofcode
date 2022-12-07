def main():
    print(calculate_answers('day06/customs_questions_0.txt'))


def calculate_answers(customs_questions):
    with open(customs_questions, 'r') as cq:
        group_answers = set()
        correct_answers = 0
        for answer in cq:
            if answer > '\n':
                for char in answer:
                    group_answers.add(char)
            else:
                group_answers.remove('\n')
                correct_answers += len(group_answers)
                group_answers.clear()

    group_answers.remove('\n')
    correct_answers += len(group_answers)
    return correct_answers


if __name__ == "__main__":
    main()
