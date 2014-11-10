#!/usr/bin/env python
import scipy.misc
import sys
import matplotlib.pyplot as plt
import numpy.testing

if (len(sys.argv) != 3):
    print "Usage python %s yfactor xfactor" % (sys.argv[0])
    sys.exit()

# load Lena image into an array
lena = scipy.misc.lena()
LENA_X = 512
LENA_Y = 512
numpy.testing.assert_equal((LENA_X, LENA_Y), lena.shape)

# Get the resize factors
yfactor = int(sys.argv[1])
xfactor = int(sys.argv[2])

# Resize Lena array
resized = lena.repeat(yfactor, axis=0).repeat(xfactor, axis=1)

numpy.testing.assert_equal((yfactor * LENA_Y, xfactor * LENA_X), resized.shape)

# plot Lena array
plt.subplot(211)
plt.imshow(lena)

plt.subplot(212)
plt.imshow(resized)
plt.show()
