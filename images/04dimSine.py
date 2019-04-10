#! /usr/bin/env python  # pylint: disable=invalid-name
"""Plot sine wave."""

from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt  # pylint: disable=import-error

# pylint: disable=useless-object-inheritance
# pylint: disable=too-few-public-methods
class PlotSine(object):
    """Plot sine wave."""

    def __init__(self):
        """Plot sine wave."""
        x = np.arange(0, 2, 0.01)
        y = x ** (-0.5) * sin(14 * pi * x)

        plt.plot(x, y)
        plt.xlabel('Time')
        plt.ylabel('f(x)')
        plt.title(r'$y=x^{-\frac{1}{2}}\sin (2\pi x)$')

        plt.show()


if __name__ == 'main':
    PlotSine()
