#
#  Illustration of functions called before each test
#   and those called before/after group of tests

import inspect
import pytest


# https://stackoverflow.com/questions/22627659/run-code-before-and-after-each-test-in-py-test
def setup_module(module):
    """ setup any state specific to the execution of the given module.
    """
    print(" * Setup_MODULE  * ")
    pass


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method."""
    print(" * TEARDOWN_module *")


def cleanup():
    print(f"\n ... {inspect.stack()[1][3]}   == Cleanup .... ==")


@pytest.fixture(autouse=False)
def run_around_tests():
    # Preparations
    print(" == PREPARATIONS == ")
    yield
    # After test
    cleanup()


def test_green():
    print(f"\n ... {inspect.stack()[1][3]}")


def test_blue():
    print(f"\n ... {inspect.stack()[1][3]}")


def test_red():
    print(f"\n ... {inspect.stack()[1][3]}")

