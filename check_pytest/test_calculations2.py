import pytest
import calculations

@pytest.mark.parametrize('x,y,result', [(3,3,6), (7,3,10), ('Hello ','Peter', 'Hello Peter')])
def test_add(x,y,result):
    assert calculations.add(x,y) == result
