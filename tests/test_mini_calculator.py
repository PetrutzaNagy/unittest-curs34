from miniCalculator import MiniCalculator


def test_sum():
    miniCalculator = MiniCalculator()
    assert miniCalculator.sum(2,3) == 5

def test_sum2():
    miniCalculator = MiniCalculator()
    assert miniCalculator.sum(3,3) == 6

def test_sum3():
    miniCalculator = MiniCalculator()
    assert miniCalculator.sum(3,0) == 3

def test_sum4():
    miniCalculator = MiniCalculator()
    assert miniCalculator.sum(0, 0) == 0