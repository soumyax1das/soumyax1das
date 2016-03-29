#!/usr/bin/env python3
"""
This library has example of string join and string split.
"""
def str_join(a,sep):
    joined_str=sep.join(a)
    return(joined_str)

def str_split(a,sep):
    SS=a.split(sep)
    return(SS)

if __name__ == '__main__':
    ###Join Strings###
    JS=str_join(['Soumya','Aarush','Paramita'],'|')
    print(JS)
    ###Split Strings###
    SS=str_split(JS,'|')
    print(SS)



