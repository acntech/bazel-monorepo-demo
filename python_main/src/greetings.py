    """Python main fail calling common python library
    """
from python_util.src.greeting_class import Greeting


def main():
    greeting_object = Greeting('Bazel')
    print(greeting_object.greet())

if __name__ == "__main__":
    main()