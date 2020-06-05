from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fibo_pass():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fibo_fail():
    actual = fibonacci(6)
    expected = 1
    assert actual != expected


def test_lucas_pass():
    actual = lucas(6, 1, 3)
    expected = 29
    assert actual == expected


def test_lucas_fail():
    actual = lucas(6, 1, 3)
    expected = 1
    assert actual != expected


def test_sum_series_not_integer_pass():
    actual = sum_series('one')
    expected = "Parameter(s) must be intergers >= 0"
    assert actual == expected


def test_sum_series_not_integer_fail():
    actual = sum_series('one')
    expected = ''
    assert actual != expected


def test_sum_series_pass():
    actual = sum_series(8, 1, 3)
    expected = 76
    assert actual == expected


def test_sum_series_fail():
    actual = sum_series(8, 1, 3)
    expected = 1
    assert actual != expected


def test_sum_series_0_pass():
    actual = sum_series(0)
    expected = 10
    assert actual == expected


def test_sum_series_0_fail():
    actual = sum_series(0)
    expected = 0
    assert actual != expected


def test_sum_series_10_pass():
    actual = sum_series(10)
    expected = 55
    assert actual == expected


def test_sum_series_10_fail():
    actual = sum_series(10)
    expected = 0
    assert actual != expected