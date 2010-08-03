#! /usr/bin/env python
from pylab import *
x=arange(0,2,0.01)
y=x**(-0.5)*sin(14*pi*x)

plot(x,y)
xlabel('Time')
ylabel('f(x)')
title(r'$y=x^{-\frac{1}{2}}\sin (2\pi x)$')

show()
