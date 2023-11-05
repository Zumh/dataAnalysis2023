#!/usr/bin/env python3


def acronyms(s):
    # split string using split
    # check length if at least two
    # all character must be upper
    # clean the word
    result = []

    # strip all the delimeter using 
    # This creates a list of ["(.,)"] repeated len(s) times.
    # This applies the str.strip() method to each word in the s.split() list and then creates a list of the results.
    result = list(map(str.strip,s.split(),["(.,)"]*len(s)))

    """
    Alter native way to clean punctuation
    import string
    # Remove punctuation from the text using the strip method
    text = text.translate(str.maketrans('', '', string.punctuation))
    """
    
    # .isupper method is checking every existing letter is upper case. Even mixed with letter
    return list(filter(lambda word : len(word) >= 2 and word.isupper(), result))

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
