#!/usr/bin/env python3

def interleave(*lists):
    result= []
    # we iterate through each element
    # *datas inside zip is turn multiple list into one list
    for data in zip(*lists):
        # we can extend each element in one list
        result.extend(data)    

    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
