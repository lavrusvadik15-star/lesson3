import pytest

@pytest.fixture(scope="session")
def browser():
    print("Браузер")
    yield
    print("закрыть браузер")

@pytest.fixture
def login_page(browser):
    print("Страница логина")
    pass

@pytest.fixture
def user():
    print("креды")
    return "username", "password"


def test_login (login_page,user):
    username, password = user
    assert username == "username"
    assert password == "password"