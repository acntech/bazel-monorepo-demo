    """Test class for Greetings class

    Raises:
        SystemExit: fix for pytest and Bazel integration (from stack)
    """
from python_util.src.greeting_class import Greeting

class TestGreeting:

    @staticmethod
    def testGreetingGreet():
        test_greeting_object = Greeting("test")
        test_greet = test_greeting_object.greet()
        assert test_greet == "Python hails test."

if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__]))