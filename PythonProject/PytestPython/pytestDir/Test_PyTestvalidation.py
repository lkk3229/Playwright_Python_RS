#Fixtures
import pytest
from pytest_playwright.pytest_playwright import playwright


@pytest.fixture(scope="module")         # if scope = "function" then it will run before every test  # if scope = "Module" then it will run once only in this whole page.
def preWork():
    print("preWork scope module")
    return "fail"

@pytest.fixture(scope="function")         # if scope = "function" then it will run before every test  # if scope = "Module" then it will run once only in this whole page.
def SecondpreWork():
    print("SecondpreWork scope function")
    yield    #pause
    print("tear down SecondpreWork scope function")

@pytest.mark.smoke
def test_initialcheck(preWork, SecondpreWork):
    print("initialcheck")
    assert preWork == "fail"

@pytest.mark.skip
def test_Secondcheck(preSetWork, SecondpreWork):
    print("test")
