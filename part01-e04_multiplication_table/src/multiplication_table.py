#!/usr/bin/env python3


def main():
    for rowNumber in range(1, 11):
        for columnNumber in range(1, 11):
            product = rowNumber * columnNumber
            # formatting the product variable with a width of four characters
            print(f"{product:4}", end="")

        print()

if __name__ == "__main__":
    main()
