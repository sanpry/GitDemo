import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self): #method
        print("i will execute fixture demo method")

    def test_fixtureDemo1(self): #method
        print("i will execute fixture demo1 method")

    def test_fixtureDemo2(self): #method
        print("i will execute fixture demo2 method")

    def test_fixtureDemo3(setup):  # method
        print("i will execute fixture demo3 method")