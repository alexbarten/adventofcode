def main():
    print(play_game("2022/day02/day02_1.txt"))


def play_game(series):
    with open(series, 'r') as rps:
        themscore, youscore = 0, 0

        for game in rps:
            them, you = make_proper(game)
            themscore += score(them)
            youscore += score(you)
            theirgame, yourgame = assess_single((them, you))
            themscore += theirgame
            youscore += yourgame

        return youscore


def make_proper(abstract_rps):
    rockpaperscissors = {"A": "rock", "B": "paper", "C": "scissors",
                         "X": "rock", "Y": "paper", "Z": "scissors"}

    them = rockpaperscissors.get(abstract_rps[0])
    you = rockpaperscissors.get(abstract_rps[2])

    return them, you


def score(hand):
    hands = {"rock": 1, "paper": 2, "scissors": 3}
    return hands.get(hand)


def assess_single(game):
    them, you = game
    if them == you:
        return 3, 3
    elif (them == "rock" and you == "scissors") or\
         (them == "scissors" and you == "paper") or\
         (them == "paper" and you == "rock"):
        return 6, 0
    elif (them == "scissors" and you == "rock") or\
         (them == "paper" and you == "scissors") or\
         (them == "rock" and you == "paper"):
        return 0, 6


if __name__ == "__main__":
    main()
