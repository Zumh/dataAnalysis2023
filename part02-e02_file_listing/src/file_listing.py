#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    # function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf")
    # re.match is for matching exactly as the input string represent. So it need to consider the rest of none match.
    pattern = r'(\d+)\s+(\w{3})\s+(\d+)\s+(\d{2}):(\d{2})\s+(.+)'
    """
    input_string = "-rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf"
    match_group = re.search(pattern, input_string)
    size, month, day, hour, minute, filename = match_group.groups()
    print(size, month, day, hour, minute, filename)
    """
    result = []
    with open(filename,"r") as file:
        for line in file:
           
            # first match all the group
            match_group = re.search(pattern, line)
            if match_group:
                size, month, day, hour, minute, filename = match_group.groups()
                result.append((int(size), month, int(day), int(hour), int(minute), filename))
            
    return result
def main():
    result = file_listing()
    print(result)
if __name__ == "__main__":
    main()
