# CSXXX Project Report: Gaussian Integration

Carla Character,
Frank Fictional,
Iris Imaginary

<sup><sub>(Spring XXXX, Professor Pat Pretend)</sub></sup>

Gaussian quadrature is a technique in numerical integration that computes an integral with the highest degree of exactness for a given number of sample points (typically called "knots").
It is known [TODO cite] that an $n$-point quadrature rule

$$\int_{-1}^1 f(x)~dx\approx \sum_{k=1}^n w_k f(x_k)$$

cannot be exact for all polynomials up to degree $2n$, by examining the polynomial $f(x)=\prod_{k=1}^n (x-x_k)^2$, which has a nonzero integral, but a quadrature result of 0. However, by the use of orthogonal polynomials, Gaussian quadrature is exact for polynomials up to degree $2n-1$, which is therefore optimal. In this project, we create a code that can produce these $w_k$, $x_k$ up to an arbitrary degree.
