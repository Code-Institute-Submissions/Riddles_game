from flask import request

# -----TESTS FRAEWORK-------#


def test_are_equal(actual,expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected,actual)

def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)


def test_is_not_in(collection, item):
    assert not item in collection, "{0} does contain {1} and it should not".format(collection, item)
