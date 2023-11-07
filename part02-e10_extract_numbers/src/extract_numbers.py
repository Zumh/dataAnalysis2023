#!/usr/bin/env python3

def extract_numbers(s):
    result = []
    for number in s.split():
        try:
            # convert to integer 
            int_number = int(number)
            result.append(int_number)
        except ValueError:
            try:
                float_number = float(number)
                result.append(float_number)
            except ValueError:
                pass
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
