import pytest
import time
from test_helper import bubble_sort
from test_helper import unsorted_list
from test_helper import print_simple_trace
from test_helper import get_total_mem_used
import tracemalloc


def inc(x):
    return x + 1


def test():
    tracemalloc.start()
    l = []
    l.extend(range(1000000))
    snapshot = tracemalloc.take_snapshot()
    print_simple_trace(snapshot)
    print(get_total_mem_used(snapshot))

