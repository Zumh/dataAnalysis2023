#!/usr/bin/env python3

def main():
    target = 5
    [print(f"({firstDie}, {secondDie})") for firstDie in range(1, 7) for secondDie in range(1,7) if firstDie + secondDie == target]

if __name__ == "__main__":
    main()
