import pytest


def test_firstProgram(setup):
    msg = "Hello"
    assert msg == "Hi", "Test Failed"


@pytest.mark.smoke
@pytest.mark.skip
def test_secondCreditCard(setup):
    print("Good Morning")


def test_newProgram(crossBrowser2):
    print(crossBrowser2)
