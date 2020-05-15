import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will execute first")  # before method
    yield
    print("i will execute last")  # after method


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["swetha", "sangeetha", "priyanka"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser1(request):
    return request.param

@pytest.fixture(params=[("chrome", "swetha", "sangeetha"), ("Firefox", "rahul"), "IE"])
def crossBrowser2(request):
    return request.param
