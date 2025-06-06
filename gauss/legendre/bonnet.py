# Compute Legendre polynomials using Bonnet's recursion formula
# (n+1)P[n+1](x) = (2*n+1) * x * P[n](x) - n * P[n-1](x)

from decimal import Decimal


def next_bonnet(
    n: int, Pn_coeffs: list[Decimal], Pnm1_coeffs: list[Decimal]
) -> list[Decimal]:
    """Computes the next polynomial of the Bonnet recursion.

    Args:
        n (int): The degree of the previous polynomial P[n]
        Pn_coeffs (list): Coefficients of P[n], in increasing degree
        Pnm1_coeffs (list): Coefficients of P[n-1], in increasing degree
    """
    coef0 = Decimal(n) / Decimal(n + 1)
    coef1 = Decimal(2 * n + 1) / Decimal(n + 1)

    Pnp1 = [-coef0 * a for a in Pnm1_coeffs]
    # add trailing zeros for x^n and x^(n+1)
    Pnp1.extend([Decimal(0)] * 2)

    for i, ai in enumerate(Pn_coeffs):
        # off-by-one handles the multiplication by x
        Pnp1[i + 1] += coef1 * ai

    return Pnp1


def legendre_polynomial(n: int) -> list[Decimal]:
    """Computes the nth degree legendre polynomial using Bonnet Recursion.

    Args:
        n (int): the degree to compute

    Returns:
        list[Decimal]: The coefficients in increasing degree of Pn
    """
    poly0 = [Decimal(1)]  # P[0] = 1
    if n == 0:
        return poly0

    poly1 = [Decimal(0), Decimal(1)]  # P[1] = x
    if n == 1:
        return poly1

    for k in range(1, n):
        # poly1 = P[k]
        poly0, poly1 = poly1, next_bonnet(k, poly1, poly0)
    return poly1
