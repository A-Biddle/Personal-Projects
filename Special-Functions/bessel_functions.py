# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 09:41:52 2020

@author: Archie
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import fmin

M_VALUES = [0]
X_VALUES = np.linspace(0,20,100)
J_VALUES = np.arange(0,100)

def bessel(x, m, j):

    output = np.array([])
    coefficients = np.array([])
    powers = np.array([])

    for value in j:
        coefficients = np.append(coefficients,
                           (((-1)**value)/(math.factorial(value)*math.factorial(m + value))*(1/2)**(m + 2*value)))
        powers = np.append(powers, (m + 2*value))

    for i in x:
        output = np.append(output, np.sum(coefficients * i ** powers))

    return output

def roots(function, tolerance=0.002):

    x_values = np.linspace(0, 20, 1000)
    function_values = function(x_values)
    guessed_roots = x_values[np.where(function_values < tolerance)]
    print(guessed_roots)
    roots = np.array([])

    for guess in guessed_roots:

        roots = np.append(roots, fmin(function, guess, disp=False)[0])

    print(roots)
    return roots

def plot(m_values, x_values, j_values):

    m_values = np.array(m_values)
    plt.figure()
    for m in m_values:
        y_values = bessel(x_values, m, j_values)

        plt.plot(x_values, y_values, label='$J_{0}(x)$'.format({m}))
        plt.hlines(0, 0, 20, linewidth=1)
        plt.xlim(0, 20)

    if len(m_values) == 1:
        root_values = roots(lambda x: np.abs(bessel(x, m_values, J_VALUES)))
        for value in root_values:
            plt.scatter(value, 0, label='{0:.2f}'.format(value))

    plt.legend(loc='upper right')
    plt.show()

def main():
    plot(M_VALUES, X_VALUES, J_VALUES)
    return 0

if __name__ == '__main__':
    main()
