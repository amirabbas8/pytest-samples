from unittest import mock
from random import randint


def sum_with_rand(number):
    return number + randint(1, 10)


@mock.patch(__name__+".randint", return_value=3, autospec=True)
def test_sum_with_rand(mock_randint):
    assert sum_with_rand(2) == 5
