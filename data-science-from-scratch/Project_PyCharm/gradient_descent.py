from collections import Counter
from linear_algebra import distance, vector_subtract, scalar_multiply
from functools import reduce, partial
import math, random

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def plot_estimated_derivative():

    def square(x):
        return x * x

    def derivative(x):
        return 2 * x

    derivative_estimate = partial(difference_quotient, square, h=0.00001)

    # plot to show they're basically the same
    import matplotlib.pyplot as plt
    x = range(-10,10)
    plt.plot(x, map(derivative, x), 'rx')           # red  x
    plt.plot(x, map(derivative_estimate, x), 'b+')  # blue +
    plt.show()

if __name__ == "__main__":

    plot_estimated_derivative()
    #
    # print("using the gradient")
    #
    # v = [random.randint(-10,10) for i in range(3)]
    #
    # tolerance = 0.0000001
    #
    # while True:
    #     #print v, sum_of_squares(v)
    #     gradient = sum_of_squares_gradient(v)   # compute the gradient at v
    #     next_v = step(v, gradient, -0.01)       # take a negative gradient step
    #     if distance(next_v, v) < tolerance:     # stop if we're converging
    #         break
    #     v = next_v                              # continue if we're not
    #
    # print("minimum v", v)
    # print("minimum value", sum_of_squares(v))
    # print()
    #
    #
    # print("using minimize_batch")
    #
    # v = [random.randint(-10,10) for i in range(3)]
    #
    # v = minimize_batch(sum_of_squares, sum_of_squares_gradient, v)
    #
    # print("minimum v", v)
    # print("minimum value", sum_of_squares(v))