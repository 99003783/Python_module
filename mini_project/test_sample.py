#import sample
from sample import add,isleap, mydiv

def test_add_one():
    assert 30 == add(10,20)
    assert 40 == add(22,18)

def test_add_two():
    assert 20 == add(0,20)
    assert 10 == add(10,0)

def test_leap_one():
    assert isleap(2012)

def test_leap_no():
assert not  isleap(2015)
     
def test_century_one():
assert not  isleap(2100)