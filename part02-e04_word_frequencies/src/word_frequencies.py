#!/usr/bin/env python3

def word_frequencies(filename):
    result = {}
    with open(filename, "r") as file:
        for input_string in file:
            lines = input_string.split()
            for word in lines:
                strip_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if strip_word not in result or not result:
                    result[strip_word] = 0
                
                result[strip_word] += 1
    return(result)

def main():
    words = word_frequencies("src/alice.txt")
    for word, frequency in words.items():
        print(f"{word}\t{frequency}")
if __name__ == "__main__":
    main()
