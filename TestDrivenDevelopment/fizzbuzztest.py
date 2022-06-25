import pytest

def fizzBuzz(value):
    if value == 3:
        return "Fizz"
    return str(value)

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")