from math import sqrt
from sys import stdin

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)
    # complex multiplication: (x+yi)(u+vi) = xu + xvi + yui + yvi^2 = (xu-yv) + (xv+yu)i
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    # http://mathworld.wolfram.com/ComplexDivision.html
    def __div__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real = float(self.real * other.real + self.imag * other.imag) / denominator
        imag = float(self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)
        
    def mod(self):
        return '{:.2f}'.format(sqrt(self.real ** 2 + self.imag ** 2))
    
    def __str__(self):
        sign = '+' if self.imag > 0 else '-'
        if self.real == 0 and self.imag == 0:
            return '0.00'
        elif self.real == 0:
            return '{:.2f}i'.format(self.imag)
        elif self.imag == 0:
            return '{:.2f}'.format(self.real)

        return '{0:.2f} {1} {2:.2f}i'.format(self.real, sign, abs(self.imag))

lines = stdin.readlines()

i = 0
while i+1<len(lines):
    line1, line2 = lines[i].strip().split(), lines[i+1].strip().split()
    a = Complex(float(line1[0]), float(line1[1]))
    b = Complex(float(line2[0]), float(line2[1]))
    print a+b
    print a-b
    print a*b
    print a/b
    print a.mod()
    print b.mod()

    i += 2
