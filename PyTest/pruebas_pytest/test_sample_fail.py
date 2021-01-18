import pytest

def func(x):
    return x + 1


def nombre(name):
    return name


def test_answer():
    assert func(5) == 5


def test_nombre():
    name = 'fernando'
    assert nombre('FERNANDO') == name()


pytest.main()
