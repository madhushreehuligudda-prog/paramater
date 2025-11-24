from add import addition
def test_add_positive_numbers():
    assert addition(2, 3) == 5
def test_add_negative_numbers():
    assert addition(-4, -6) == -5
def test_add_zero():
    assert addition(0, 5) == 5
    assert addition(5, 0) == 5
