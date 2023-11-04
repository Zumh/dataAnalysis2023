#!/usr/bin/env python3

def triple(number):
    return number * 3

def square(number):
    return number ** 2
def main():
    triple_product =0
    square_product = 0
    for number in range(1, 11):
        triple_product = triple(number)
        square_product = square(number)
        if square_product > triple_product:
            break
        print(f"triple({number})=={triple_product} square({number})=={square_product}")

if __name__ == "__main__":
    main()
