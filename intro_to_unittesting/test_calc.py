from simple_calc import SimpleCalc
import pytest

calc = SimpleCalc()

def test_add():
    assert calc.add(2, 2) == 4

def test_subtract():
    assert calc.subtract(4, 1) == 3

def test_multiply():
    assert calc.multiply(2, 2) == 4
