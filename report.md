# CSXXX Project Report: Gaussian Integration

Carla Character,
Frank Fictional,
Iris Imaginary

<sup><sub>(Spring XXXX, Professor Pat Pretend)</sub></sup>

Gaussian quadrature is a technique in numerical integration that computes an integral with the highest degree of exactness for a given number of sample points (typically called "knots").
It is known [TODO cite] that an $n$-point quadrature rule

$$\int_{-1}^1 f(x)~dx\approx \sum_{k=1}^n w_k f(x_k)$$

cannot be exact for all polynomials up to degree $2n$, by examining the polynomial $f(x)=\prod_{k=1}^n (x-x_k)^2$, which has a nonzero integral, but a quadrature result of 0. However, by the use of orthogonal polynomials, Gaussian quadrature is exact for polynomials up to degree $2n-1$, which is therefore optimal. In this project, we create a code that can produce these $w_k$, $x_k$ up to an arbitrary degree.

## Legendre Polynomials

Legendre Polynomials are the orthogonal polynomials on the interval $[-1,1]$. Up to scalar multiples, the sequence $(P_k)_{k=0}^\infty$, where $P_k$ is of degree $k$ and orthogonal to polynomials of all lower degree, is unique.
We can compute them using the Bonnet recursion formula

$$(n+1)P_{n+1}(x) = (2n+1) x P_n(x) - nP_{n-1}(x),$$

where we can take $P_0(x) = 1$ and $P_1(x) = x$. This sequence is scaled so that $P(1)$ is always $1$.

> [!NOTE]
> I think we need to show why this is orthogonal.
