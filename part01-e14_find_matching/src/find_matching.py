#!/usr/bin/env python3

def find_matching(L, pattern):
    result = []
    for index, word in enumerate(L):
        if pattern in word:
            result.append(index)
    return result
def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en") 
    print(result)

if __name__ == "__main__":
    main()
