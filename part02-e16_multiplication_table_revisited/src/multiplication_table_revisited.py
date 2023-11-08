#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    first = np.arange(n).reshape((n,1))
    second = np.arange(n).reshape((n,))

    return np.array(first * second)
def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
