from decimal import Decimal
from decimal import getcontext as decimalcontext
from fractions import Fraction
from itertools import zip_longest

import pytest

from gauss.legendre.bonnet import legendre_polynomial


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
    for k, coefs in enumerate(zip_longest(p, ptrue, fillvalue=0)):
        a, atrue = coefs
        assert abs(a - atrue) < tol, (
            f"degree {k} coefficient not equal:\n"
            f"computed: {a} x**{k}\n  actual: {atrue} x**{k}"
        )


def test_leg0(precision):
    _assert_poly_close(legendre_polynomial(0), [1], precision)


def test_leg1(precision):
    _assert_poly_close(legendre_polynomial(1), [0, 1], precision)


def test_leg2(precision):
    _assert_poly_close(
        legendre_polynomial(2), [-Decimal("0.5"), 0, Decimal("1.5")], precision
    )


def test_leg3(precision):
    _assert_poly_close(
        legendre_polynomial(3), [0, -Decimal("1.5"), 0, Decimal("2.5")], precision
    )


def test_leg4(precision):
    eighth = 1 / Decimal(8)
    _assert_poly_close(
        legendre_polynomial(4),
        [Decimal(3) * eighth, 0, -Decimal(30) * eighth, 0, Decimal(35) * eighth],
        precision,
    )
