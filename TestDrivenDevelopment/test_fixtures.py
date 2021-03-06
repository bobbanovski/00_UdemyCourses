import pytest

# @pytest.fixture(autouse=True)
@pytest.fixture()
def setup1():
    print("\nSetup 1")
    # Yield keyword - used when Fixture goes out of scope (teardown)
    # in this case used once per test
    yield
    print("\nTeardown1")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

# def test1(setup):
def test1(setup1):
    print("\nExecuting test1")
    assert True

# @pytest.mark.usefixtures("setup")

def test2(setup2):
    print("\nExecuting test2")
    assert True