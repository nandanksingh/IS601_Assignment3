""" tests/test_operations.py
Unit tests for the Operations class using pytest parameterization.
Covers addition, subtraction, multiplication, division, and division-by-zero.
"""

import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]

# Addition
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ],
    ids=["two_positive", "zeros", "neg_pos", "two_floats", "neg_float_pos_float"]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected


# Subtraction
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected


# Multiplication
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-2, -3, 6),
        (2.5, 4.0, 10.0),
        (-2.5, 4.0, -10.0),
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected


# Division
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (6.0, -3.0, -2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    result = Operations.division(a, b)
    assert result == expected


# Division by zero
@pytest.mark.parametrize(
    "a, b",
    [(1, 0), (-1, 0), (0, 0)],
    ids=["pos_by_zero", "neg_by_zero", "zero_by_zero"]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(a, b)
