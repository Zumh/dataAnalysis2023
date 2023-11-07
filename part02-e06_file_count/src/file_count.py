#!/usr/bin/env python3

import sys

def file_count(filename):
    lines_total, words_total, characters_total = 0, 0, 0
    # count the number of lines, words, and characters in the file
    with open(filename, "r") as file:
        for line in file:
            
            characters_total += len(line)
            words_total += len(line.split())
            lines_total += 1    

    return (lines_total, words_total, characters_total)   
 

def main():
    #filenames = ["src/test.txt"]
    for filename in sys.argv[1:]:
    #for filename in filenames:
        linecount, wordcount, charactercount = file_count(filename)
        print(f"{linecount}\t{wordcount}\t{charactercount}\t{filename}")


if __name__ == "__main__":
    main()
