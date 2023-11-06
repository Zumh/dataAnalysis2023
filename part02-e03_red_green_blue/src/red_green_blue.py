#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    # input string need to be 
    """
    ! $Xorg: rgb.txt,v 1.3 2000/08/17 19:54:00 cpqbld Exp $
    255 250 250		snow
    """
    # get rid off the head
    # replace all the single space with \t
    # it matches all the single space and we replace them with \t character
    # input_string = "255 250 250		snow"

    with open(filename, "r") as file:
        # we skip the first line
        first_line = file.readline()
        result = []
      
        # we iterate through the line
        for line in file:
            #line = "255 250 250		snow white"
          
            newstr = re.search(r'(\d+)\s+(\d+)\s+(\d+)\s+(\w+.*)', line)
           
            # newstr = re.sub(r'(\d+)\s+', r'\1\\t', line)
            # 255\t250\t250\tsnow
            # eliminate new line at the end
            result.append(("\t".join(newstr.groups())).strip())
    return result


def main():
    result = red_green_blue()
    print(result)
if __name__ == "__main__":
    main()
