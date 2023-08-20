# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:40:14 2020

@author: Archie
"""
import numpy as np
import matplotlib.pyplot as plt
import math

X_VALUES = np.linspace(-1.2, 1.2, 100)
N_VALUES = [0,1,4,5,10]

def binomial_coefficient(n, k):
    return (math.factorial(n))/(math.factorial(k) * math.factorial(n - k))

def legendre_polynomial(n, x_values):

    coefficient_values = np.array([])
    output = np.array([])

    k = 0
    k_values = np.array([])

    while k <= n:
        coefficient_values = np.append(coefficient_values,
                                  binomial_coefficient(n, k) *
                                  binomial_coefficient(n + k, k))
        k_values = np.append(k_values, k)
        k += 1

    for i in x_values:
        output = np.append(output, np.sum(coefficient_values * ((i - 1)/2) ** k_values))

    return output

def plot(n_values, x_values):

    plt.figure()

    for n in n_values:
        y_values = legendre_polynomial(n, x_values)

        plt.plot(x_values, y_values,
                 label='P$_{0}$'.format({n}))

    plt.legend()
    plt.hlines(0, -1.2, 1.2, linewidth=1)
    plt.vlines(0, -1.2, 1.2, linewidth=1)
    plt.ylim(-1.2, 1.2)
    plt.xlim(-1.2, 1.2)
    plt.show()

def main():

    plot(N_VALUES, X_VALUES)

    return 0

if __name__ == '__main__':
    main()