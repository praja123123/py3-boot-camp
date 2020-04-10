import pytest
import calculations

@pytest.mark.number
def test_add():
    assert calculations.add(3,3) == 6
    assert calculations.add(7) == 10
    assert calculations.add(9,9) == 18

@pytest.mark.number
def test_multiply():
    assert calculations.multiply(3,3) == 9
    assert calculations.multiply(5) == 15
    assert calculations.multiply(6,10) == 60
    assert calculations.multiply(4,4) > 15

@pytest.mark.string
def test_add_string():
    assert calculations.add('Hello', ' world!') == 'Hello world!'
    assert type(calculations.add('Hello', ' world!')) is str

@pytest.mark.string
def test_multiply_string():
    assert calculations.multiply('dupa') == 'dupadupadupa'
    print('---Check multiplied strings---', calculations.multiply('dupa'))