def main():
    print(convert_input("day02/day02_1.txt"))


def convert_input(rpsfile):
    with open(rpsfile, 'r') as rps:
        translator = {"A X": "A Z", "A Y": "A X", "A Z": "A Y",
                      "B X": "B X", "B Y": "B Y", "B Z": "B Z",
                      "C X": "C Y", "C Y": "C Z", "C Z": "C X"}
        scores = {"A X": [4, 4], "A Y": [1, 8], "A Z": [7, 3],
                  "B X": [8, 1], "B Y": [5, 5], "B Z": [2, 9],
                  "C X": [3, 7], "C Y": [9, 2], "C Z": [6, 6]}

        themscore, youscore = 0, 0

        for entry in rps:
            translated = translator.get(entry.rstrip())
            them, you = scores.get(translated)

            themscore += them
            youscore += you

        return youscore


if __name__ == "__main__":
    main()
