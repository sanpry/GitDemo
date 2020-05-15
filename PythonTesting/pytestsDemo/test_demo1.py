import pytest


def test_firstProgram(setup):
    print("hello")

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Good morning")

@pytest.mark.xfail
def test_secondMobileCreditCard(setup):
    a = 2
    b = 4
    assert a+b == 6, "sum of two variables is equal to 6"