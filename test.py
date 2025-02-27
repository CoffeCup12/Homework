import pytest
import main
import random 

def testEmpty():
    test = []
    main.sort(test,0,len(test))
    assert test == []

def testDuplicate():
    test = [5, 5, 7]
    org = test.copy()
    main.sort(test, 0, len(test))
    assert test == sorted(org)

def testNormal():
    test = [random.randint(1, 100) for _ in range(100)]
    org = test.copy()
    main.sort(test, 0, len(test))
    assert test == sorted(org)
