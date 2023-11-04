#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):

    import math
    plus_value = 0
    subtract_value = 0
    denominator = (2 * a)
    result = (plus_value, subtract_value)
    sqrt_value = math.sqrt(b ** 2 - (4*a*c))
    b *= -1
    plus_value = (b + sqrt_value) / denominator
    subtract_value = (b - sqrt_value) / denominator

    result = (plus_value, subtract_value)
    return result


def main():
    pass

if __name__ == "__main__":
    main()
