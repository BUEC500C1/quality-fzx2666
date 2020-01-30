import hw1
import pytest

def test_container():
    assert hw1.intToRoman(1) == 'I'
    assert hw1.intToRoman(3150) == 'MMMCL'
