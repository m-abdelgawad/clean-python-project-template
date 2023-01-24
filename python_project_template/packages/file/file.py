import os
import inspect


def get_caller_path():
    # Get absolute path of the caller module
    return inspect.stack()[1].filename


def get_caller_parent():
    # Get absolute path of the caller module
    caller_abs_path = inspect.stack()[1].filename
    return os.path.dirname(caller_abs_path)


if __name__ == "__main__":
    print(get_caller_path())
