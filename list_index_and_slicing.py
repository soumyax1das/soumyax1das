#!/usr/bin/env python3
def string_index_example(lst,indx):
    print('Actual String is -',lst)
    print('Value at index',indx,'is',lst[indx])


def string_slice(lst):
    print(lst[-2:-1])
    print(lst[-2:])


if __name__ == '__main__':
    str="Hello this is Soumya Das"
    ###Create a list from a string###
    lst=list(str.split())
    string_index_example(lst,3)
    string_index_example(lst,-1)
    string_slice(lst)