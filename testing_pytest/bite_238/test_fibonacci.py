import pytest

from .fibonacci import fib


def test_fib_with_negative():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_special_cases():
    assert 0 == fib(0)
    assert 1 == fib(1)
    assert 1 == fib(2)


def test_fib_with_float():
    with pytest.raises(ValueError):
        fib(2.1)


def test_fib_with_low_integer():
    assert 2 == fib(3)


def test_fib_with_high_integer():
    with pytest.raises(RecursionError):
        fib(1_000_000_000_000_000_000)
