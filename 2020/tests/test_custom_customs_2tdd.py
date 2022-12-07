from day06.custom_customs_2_with_tdd import count_answers


def test_single_answers():
    result = count_answers(['x'])
    assert result == 1

    result = count_answers(['abc'])
    assert result == 3

    result = count_answers(['aaaa'])
    assert result == 1

    result = count_answers(['aaaaaaaaaaaaz'])
    assert result == 2


def test_count_group():
    result = count_answers(['a', 'a', 'a', 'a'])
    assert result == 1

    result = count_answers(['a', 'ab', 'a', 'a'])
    assert result == 1

    result = count_answers(['a', 'b', 'c'])
    assert result == 0

    result = count_answers(['aauehwns', 'snwhueaa'])
    assert result == 7
