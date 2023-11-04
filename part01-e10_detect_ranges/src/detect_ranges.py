#!/usr/bin/env python3

def detect_ranges(L):
    # sort the list
    # 2, 4, 5, 6, 7, 8, 10, 12, 13
    nums = sorted(L)
    start = end = nums[0]
    result = []
    # check the range of sorted array
    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            # detect if we are getting a single digit
            if start == end:
                result.append(start)
            else: # detect if we are in a range
                result.append((start, end + 1)) 
            start = end = num
    
    # if we have a single digit without range then append that
    if start == end:
        result.append(start)
    else: # if we have a final range append that in a tuple form
        result.append((start, end + 1))
    return result 

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
