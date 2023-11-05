#!/usr/bin/env python3

def transform(s1, s2):
    first = list(map(int, s1.split()))
    second = list(map(int, s2.split()))
    return [x * y for x, y in zip(first, second)]
    #return list(map(lambda x, y: x * y, first, second))

def main():
    s1, s2 = "1 5 3", "2 6 -1"
    result = transform(s1, s2)
    print(result)

if __name__ == "__main__":
    main()
