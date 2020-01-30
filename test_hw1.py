import hw1
import pytest

def test_container():
    a = [1,100,1000,1500,2000,2500,3000]
    b = ['I','C','M','MD','MM','MMD','MMM']
    for x,y in zip(a,b):
        assert hw1.intToRoman(x) == y
