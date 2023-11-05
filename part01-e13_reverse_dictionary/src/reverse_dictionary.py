#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
   
    for key, values in d.items():
        for value in values:
          
            # check if current value is in a new result key list
            # if exist we have synonymous
            if value in result.keys():
                result[value].append(key)
            else:
                result[value] = [key]
    return result


def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    result = reverse_dictionary(d)
    print(result)

if __name__ == "__main__":
    main()
