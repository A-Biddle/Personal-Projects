# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:45:31 2021

@author: Archie
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

def plot(function, xmin, xmax, file_name, label, parity=0):

    x_values = np.linspace(xmin, xmax, 1000)
    y_values = function(x_values)

    ymin, ymax = 1.1*np.min(y_values), 1.1*np.max(y_values)

    if ymin == 0:
        ymin = -0.1*ymax

    figure = plt.figure()
    axis = figure.add_subplot(111)
    axis.plot(x_values, y_values, label='{0}$(x)$'.format(str(label)))
    axis.plot(x_values, fourier_approximation([1, 2, 3, 4, 5, 6], function, 6, x_values, parity))
    axis.legend()

    plt.hlines(0, xmin, xmax, linewidth=1, color='k')
    plt.vlines(0, ymin, ymax, linewidth=1, color='k')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.savefig('{0}.png'.format(file_name), dpi=300)

    return plt.show()

def fourier_approximation(n_values, function, period, x_values, parity):
    """
    parity: 0 = even, 1 = odd.
    """

    output_values = np.full(len(x_values), (2/period)*integrate.quad(function, -period/2, period/2)[0])

    for n in n_values:

        if parity == 0:
            coefficient = (2/period)*integrate.quad(lambda x : function(x) * np.cos(2*n*np.pi*x/period), -period/2, period/2)[0]
            output_values += coefficient*np.cos(2*n*np.pi*x_values/period) + coefficient

        elif parity == 1:
            coefficient = (2/period)*integrate.quad(lambda x : function(x) * np.sin(2*n*np.pi*x/period), -period/2, period/2)[0]

            output_values += coefficient*np.sin(2*n*np.pi*x_values/period)

    return output_values

plot(lambda x: x**3 + x, -3, 3, 'x_squared', 'f', parity=1)
