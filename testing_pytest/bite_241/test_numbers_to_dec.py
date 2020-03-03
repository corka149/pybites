import pytest

from .numbers_to_dec import list_to_decimal


def test_list_to_decimal_with_invalid_types():
    with pytest.raises(TypeError):
        list_to_decimal([2, 1.1, 4])
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, True])
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, '3'])


def test_list_to_decimal_out_of_range():
    with pytest.raises(ValueError):
        list_to_decimal([-1])
    with pytest.raises(ValueError):
        list_to_decimal([0, 1, 10])


def test_list_to_decimal_with_empty_list():
    with pytest.raises(ValueError):
        list_to_decimal([])


def test_list_to_decimal_with_valid_decimals():
    assert 1 == list_to_decimal([1])
    assert 13 == list_to_decimal([1, 3])
    assert 137 == list_to_decimal([1, 3, 7])
    assert 1379 == list_to_decimal([1, 3, 7, 9])
    assert 13790 == list_to_decimal([1, 3, 7, 9, 0])
