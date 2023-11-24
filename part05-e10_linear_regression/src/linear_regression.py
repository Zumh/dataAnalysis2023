#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    #  The function should return the tuple (slope, intercept) of the fitted line. 
    model_line=LinearRegression(fit_intercept=True)
    
    model_line.fit(x[:, np.newaxis], y)
  
    slope = model_line.coef_[0]
    intercept = model_line.intercept_    
    return slope, intercept
    
def main():
    x = np.array([1,2,3])
    y = np.array([4,5,6])
    
    slope, intercept = fit_line(x,y)
    print(f"Slope: {slope}\nIntercept: {intercept}")
    model=LinearRegression(fit_intercept=True)
    
    model.fit(x[:, np.newaxis], y)
    # plot original data points and new data points
    xfit = np.linspace(0, 10, 100)
    yfit = model.predict(xfit[:, np.newaxis])
    plt.plot(x, y, color="Red")
    plt.plot(xfit, yfit, color="black")
    plt.show()
if __name__ == "__main__":
    main()
