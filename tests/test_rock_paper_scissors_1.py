import pytest

from day02.rock_paper_scissors_1_tdd import assess_single, make_proper, score


@pytest.mark.parametrize("rock_paper_scissors, them, you",
                         [("A X", "rock", "rock"), ("B Y", "paper", "paper"),
                          ("C Z", "scissors", "scissors"),
                          ("A Y", "rock", "paper")])
def test_make_proper(rock_paper_scissors, them, you):
    first, second = make_proper(rock_paper_scissors)
    assert first == them and second == you


@pytest.mark.parametrize("hand,value",
                         [("rock", 1), ("paper", 2), ("scissors", 3)])
def test_score(hand, value):
    result = score(hand)
    assert result == value


@pytest.mark.parametrize("game, them, you",
                         [(("rock", "rock"), 3, 3),
                          (("scissors", "paper"), 6, 0),
                          (("paper", "scissors"), 0, 6)])
def test_assess_single(game, them, you):
    themscore, youscore = assess_single(game)
    assert themscore == them and youscore == you
