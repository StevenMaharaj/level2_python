from app.calculator import add, divide

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(1, 0)