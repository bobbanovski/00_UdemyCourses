import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")
    # Yield keyword - used when Fixture goes out of scope (teardown)
    # in this case used once per test
    yield
    print("\nTeardown")

# def test1(setup):
def test1():
    print("\nExecuting test1")
    assert True

# @pytest.mark.usefixtures("setup")
def test2():
    print("\nExecuting test2")
    assert True