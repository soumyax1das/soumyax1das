#!/usr/bin/env python3
"""
    Library :: words
    Function :: a,b,c
    Author :: Soumya Das
"""
import sys
from urllib.request import urlopen


def read_url(url):
    """
    Fetch all words from a given url.

    Args::
    url

    Returns::
    Array of words, decoded in UTF-8 from the url.

    Developer::
    Soumya Das
    """
    with urlopen(url) as story:
        story_words=[]
        for line in story:
            line_words=[]
            line_words=line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)

    """
    Return the collection of words.
    """
    return story_words


def print_words(story_words):
    print('--------Going to print content of the url-----------')
    for w in story_words:
        print(w)
    print('--------Finished printing----------')


def main(url):
    print_words(read_url(url))


if __name__ == '__main__':
    #'http://sixty-north.com/c/t.txt'
    #main(sys.argv[1])
    main('http://sixty-north.com/c/t.txt')