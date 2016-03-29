"""
 Pangrams are strings containing every letter of the Alphabet.
 This program has a function that checks if a string is a pangram or not.
"""

import string
def is_pangram(my_string):
    master_alphabet=string.ascii_lowercase
    print(master_alphabet)
    found=[my_string.lower().count(l) for l in master_alphabet]
    print(found)
    if found.count(0)>0:
        return(False)
    else:
        return(True)
if __name__ == '__main__':
    print(is_pangram('a quick brown fox jumps over the lazy dog'))
    print(is_pangram('Soumya'))
