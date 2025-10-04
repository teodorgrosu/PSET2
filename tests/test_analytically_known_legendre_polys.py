<<<<<<< HEAD
from decimal import Decimal
from itertools import zip_longest

import pytest

from gauss.legendre.bonnet import legendre_polynomial


<<<<<<< HEAD
@pytest.fixture(params=[5, 10, 100, 1000])
def precision(request):
    prec = request.param
    decimalcontext().prec = prec + 1
    return prec


def poly_fraction_to_decimal(p: list[Fraction]) -> list[Decimal]:
    return [a.numerator / Decimal(a.denominator) for a in p]


def _assert_poly_close(p, ptrue, prec):
    tol = Decimal(10) ** (-prec)
    p = poly_fraction_to_decimal(p)
=======
def _assert_poly_equals(p, ptrue):
>>>>>>> rational-legendre
    for k, coefs in enumerate(zip_longest(p, ptrue, fillvalue=0)):
        a, atrue = coefs
        assert a == atrue, (
            f"degree {k} coefficient not equal:\n"
            f"computed: {a} x**{k}\n  actual: {atrue} x**{k}"
        )


def test_leg0():
    _assert_poly_equals(legendre_polynomial(0), [1])


def test_leg1():
    _assert_poly_equals(legendre_polynomial(1), [0, 1])


def test_leg2():
    _assert_poly_equals(legendre_polynomial(2), [-Fraction(1, 2), 0, Fraction(3, 2)])


def test_leg3():
    _assert_poly_equals(
        legendre_polynomial(3), [0, -Fraction(3 / 2), 0, Fraction(5, 2)]
    )


def test_leg4():
    eighth = Fraction(1, 8)
    _assert_poly_equals(
        legendre_polynomial(4), [3 * eighth, 0, -30 * eighth, 0, 35 * eighth]
    )
