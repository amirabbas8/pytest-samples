import sys
import pytest


@pytest.mark.skipif()
def test_skipped():
    assert 1


@pytest.mark.skipif(sys.version_info[0] == 3, reason="Only Python 2")
def test_skipped_if():
    assert 1
