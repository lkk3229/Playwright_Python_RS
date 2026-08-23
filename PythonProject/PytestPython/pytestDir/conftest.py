import pytest


@pytest.fixture(scope="session")  # if scope = "session" then it will run only once before every test
def preSetWork():
    print("preSetWork scope session")
