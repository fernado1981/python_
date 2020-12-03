import pytest


def func(x):
    return x + 1


def nombre(name):
    return name


def test_answer():
    assert func(4) == 5


def test_nombre():
    name = 'fernando'
    assert nombre('fernando') == name.lower()


pytest.main()
