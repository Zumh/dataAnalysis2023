#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, r2):
        numerator = self.numerator*r2.denominator + self.denominator*r2.numerator
        denominator = self.denominator*r2.denominator
        return Rational(numerator, denominator)

    def __sub__(self, r2):
        numerator = self.numerator*r2.denominator - self.denominator*r2.numerator
        denomenator = self.denominator*r2.denominator
      
        return Rational(numerator, denomenator)
    def __mul__(self, r2):
        mul_rational = Rational(self.numerator*r2.numerator, self.denominator*r2.denominator)
        return mul_rational
    def __truediv__(self, r2):
        div_rational = Rational(self.numerator*r2.denominator, self.denominator*r2.numerator)
        return div_rational
    
    def __lt__(self, r2):
        return (self.numerator/self.denominator) < (r2.numerator/r2.denominator)
    
    def __gt__(self, r2):
        return (self.numerator/self.denominator) > (r2.numerator/r2.denominator)
    
    def __eq__(self, r2):
        return (self.numerator/self.denominator) == (r2.numerator/r2.denominator)
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)

    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
