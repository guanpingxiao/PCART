import scipy.integrate as spi

def f(x):
    return x ** 2
(result, error) = spi.quad_vec(f, a=0, b=1, args=())