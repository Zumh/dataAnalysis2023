#!/usr/bin/env python3

import sys
import math
def summary(filename):
    # return a triple with the sum, average, and standard deviation
  
    
    converted_numbers = []
    (total_sum,average_number,standard_deviation) = (0,0,0)

    with open(filename, 'r') as file:
        # conversion
        for number in file.read().split():
            try:
                converted_numbers.append(float(number))
            except ValueError:
                continue

        #convert_number = list(map(float, input_numbers.split()))
        total_sum = sum(converted_numbers)
        length = len(converted_numbers)
        mean = average_number = total_sum/length
        sum_of_diff = 0

        
        for number in converted_numbers:
            square_diff = (number - mean)**2
            sum_of_diff += square_diff
        variance = sum_of_diff / (length - 1)
        standard_deviation = math.sqrt(variance)

   
 

    return (total_sum,average_number,standard_deviation)

def main():
    for filename in sys.argv[1:]:
        (total_sum,average_number,standard_deviation) = summary(filename)
        print(f"File: {filename} Sum: {total_sum:0.6f} Average: {average_number:0.6f} Stddev: {standard_deviation:0.6f}")


if __name__ == "__main__":
    main()
