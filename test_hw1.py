import hw1
import pytest

print(hw1.intToRoman(4000))

def test_container():
    a = [1,100,1000,1500,2000,2500,3000,4000,35.6,'a','-1']
    b = ['I','C','M','MD','MM','MMD','MMM','MMMM',-1,-1,-1]
    for x,y in zip(a,b):
        assert hw1.intToRoman(x) == y

def main():
    test_container()

if __name__== "__main__":
    main()
