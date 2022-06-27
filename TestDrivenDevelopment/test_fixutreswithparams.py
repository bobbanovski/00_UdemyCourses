import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    # pytest will go through each element in the list and run a test with each
    # allows looping in tests for multiple inputs
    retVal = request.param
    print("\nSetup retVal = {}".format(retVal))
    return retVal

def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True