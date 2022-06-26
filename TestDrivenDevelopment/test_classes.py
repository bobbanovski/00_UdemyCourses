class TestClass:
    @classmethod
    def setup_class(cls):
        # Run before all methods in class test
        print("\nSetup TestClass")

    @classmethod
    def teardown_class(cls):
        # Run at the conclusion of all method testing in this class
        print("\nTeardown TestClass")

    def setup_method(self, method):
        if method == self.test_me:
            print("\nSetting up test_me")
        elif method == self.test_me2:
            print("\nSetting up test_me2")
        else:
            print("\nSetting up unknown test")

    def teardown_method(self, method):
        if method == self.test_me:
            print("\nTearing down test_me")
        elif method == self.test_me2:
            print("\nTearing down test_me2")
        else:
            print("\nTearing down unknown test")



    def test_me(self):
        print("\nExecuting Test1")
        assert True

    def test_me2(self):
        print("\nExecuting Test2")
        assert True

class MyTestClass:
    # This class ignored because it doesn't follow standard naming convention starting in Test
    def test_it(self):
        assert True

    def test_it2(self):
        assert True