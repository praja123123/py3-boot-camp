import my_sum
import pytest

@pytest.mark.parametrize("x,y,z,w",[(1,2,3,6), (4,5,6,15)])

def test_my_sum1(x,y,z,w):
    result = my_sum.my_sum((x,y,z))
    assert result == w

def test_my_sum2():
    result = my_sum.my_sum((1,2,3))
    assert result == 6