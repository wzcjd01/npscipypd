#!/usr/bin/env python
__author__ = 'Wang Zhicheng'

import numpy as np
import matplotlib.pyplot as plt


def triangle_wave(x, c, c0, height):
    x = x - int(x)  # period of this wave is 1
    if x >= c:
        r = .0
    elif x < c0:
        r = x * height / c0
    else:
        r = (c - x) * height / (c - c0)

    return r


triangle_ufunc = np.frompyfunc(lambda x: triangle_wave(x, .6, .4, 1.0), 1, 1)

x = np.linspace(0, 8, 1000)
y = triangle_ufunc(x)

plt.plot(x, y)
plt.show()