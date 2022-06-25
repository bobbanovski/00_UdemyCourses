import pytest

def fizzBuzz(value):
    return("1")

def test_canAssertTrue():
    assert True

def test_canCallFizzBuzz():
    fizzBuzz(1)

def test_returns1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == "1"