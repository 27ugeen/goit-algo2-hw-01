import pytest
from find_min_max import find_min_max

def test_find_min_max():
    assert find_min_max([3, 1, 5, 2, 4]) == (1, 5)
    assert find_min_max([10, 20, 30, 40, 50]) == (10, 50)
    assert find_min_max([100]) == (100, 100)
    assert find_min_max([-10, -5, -1, -20]) == (-20, -1)
    assert find_min_max([7, 7, 7, 7]) == (7, 7)
    assert find_min_max([1, -1]) == (-1, 1)

    with pytest.raises(ValueError):
        find_min_max([])