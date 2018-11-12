import pytest
import time
from TestHelper import bubble_sort
from TestHelper import print_simple_trace
from TestHelper import unsorted_list


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5