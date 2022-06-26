class TestClass:
    def test_me(self):
        assert True

    def test_me2(self):
        assert True

class MyTestClass:
    # This class ignored because it doesn't follow standard naming convention starting in Test
    def test_it(self):
        assert True

    def test_it2(self):
        assert True