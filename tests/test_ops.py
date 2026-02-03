from ..src.ops import add, sub

def test_add():
    assert add(10, 2) == 12
    assert add(2, 3) == 5
    assert add(-1, 10) == 9

def test_sub():
    assert sub(4, 3) == 1
    assert sub(2, 3) == -1
    assert sub(12, 10) == 2