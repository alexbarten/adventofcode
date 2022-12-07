def main():
    print(calculate_seat('day06/customs_questions_0.txt'))


def calculate_seat(customs_questions):
    with open(customs_questions, 'r') as cq:
        all_answers = set()
        line_answers = set()
        correct_answers = 0
        for answer in cq:
            if answer > '\n':
                for char in answer:
                    line_answers.add(char)
                if len(all_answers) > 0:
                    all_answers = all_answers.intersection(line_answers)
                else:
                    all_answers = line_answers
                line_answers.clear()
            else:
                if '\n' in all_answers:
                    all_answers.remove('\n')
                correct_answers += len(all_answers)
                line_answers.clear()
                all_answers.clear()

    if '\n' in all_answers:
        all_answers.remove('\n')
    correct_answers += len(all_answers)
    return correct_answers


if __name__ == "__main__":
    main()
