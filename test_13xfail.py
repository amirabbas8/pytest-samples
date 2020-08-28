import pytest


def division(a, b):
    try:
        return a / float(b)
    except ZeroDivisionError:
    # except RecursionError:
        return 1


@pytest.mark.xfail
def test_division_fail():
    assert division(1, 0) == 1
