from implementation.eight_kata import EightKata


eight_kata = EightKata()


def test_liters():
    assert eight_kata.liters(3) == 1
