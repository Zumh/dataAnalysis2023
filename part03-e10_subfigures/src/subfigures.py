#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    left_x, left_y = a[:,0], a[:,1]
       
    plt.subplot(1, 2, 1)
    plt.plot(left_x, left_y)
    plt.title("graph-title")
    plt.xlabel("graph-x-axis")
    plt.ylabel("graph-y-axis")
    
 
    plt.subplot(1, 2, 2)
    plt.scatter(a[:,0], a[:,1],c=a[:,2], s=a[:,3])
    plt.title("scatter-title")
    plt.xlabel("scater-x-axis")
    plt.ylabel("scater-y-axis")
    plt.show()
def main():
    pass
    """
    n = 10
    a = np.random.randint(0, 10, (n, 3))
    a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    """
    subfigures(a)
if __name__ == "__main__":
    main()
