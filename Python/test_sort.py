import pytest
import tracemalloc
from sort import inc
from test_helper import print_simple_trace


def test_answer():
    assert inc(3) == 6
