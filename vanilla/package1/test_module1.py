import pytest
from .module1 import Class1


# Fixtures are useful to write less code
@pytest.fixture
def class1_reversed():
    """Returns a class1 instance with a is_reversed parameter set to True"""
    return Class1(is_reversed=True)


@pytest.fixture
def class1_not_reversed():
    """Returns a class1 instance with a is_reversed parameter set to False"""
    return Class1(is_reversed=False)


# Use of number 1 fixture
def test_compute_length_reversed(class1_reversed):
    assert class1_reversed.compute_length("Fanch") == 5


def test_first_character_reversed(class1_reversed):
    assert class1_reversed.get_first_character("Fanch") == "h"


# Use of number 2 fixture
def test_compute_length_not_reversed(class1_not_reversed):
    assert class1_not_reversed.compute_length("Fanch") == 5


def test_first_character_not_reversed(class1_not_reversed):
    assert class1_not_reversed.get_first_character("Fanch") == "F"


# Parametrized tests
@pytest.mark.parametrize("is_reversed,name,expected", [(True, "Fanch", "Hello hcnaF !"),
                                                       (False, "Andrew", "Hello Andrew !"),
                                                       (True, "hannah", "Hello hannah !")])
def test_say_hello(is_reversed, name, expected):
    my_class = Class1(is_reversed)
    assert my_class.say_hello(name) == expected
