#!/usr/bin/env python3

def merge(L1, L2):
    result = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        # merge data from L1 to L2
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    if i < len(L1):
        result.extend(L1[i:])
    elif j < len(L2):
        result.extend(L2[j:])
         
    return result
def main():
    L1 = [2,3,7,8]
    L2 = [9,18,4,6]
   
    L = merge(sorted(L1), sorted(L2))
    print(L)
    if len(L) == len(L1) + len(L2):
        print("sorted")
    else:
        print("not sorted")

if __name__ == "__main__":
    main()
