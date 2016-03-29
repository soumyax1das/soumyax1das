#!/usr/bin/env python3
"""
This function library is written to test use cases with tuples
"""
def find_min_max(inp_tuple):
    mn=min(inp_tuple)
    mx=max(inp_tuple)
    return(mn,mx)

def swap_tuple(it):
    ###Tuple Unpacking###
    c,d=it
    d,c=c,d
    return(c,d)
if __name__ == '__main__':
    ###Tuple unpacking###
    n,x=find_min_max((1,2,3,4,5))
    print('Lowest No in the tuple is',n)
    print('Max No in the tuple is',x)
    ###Tuple Constructor :: Tuple from List###
    it=tuple([x,n])
    print(it)
    it=swap_tuple(it)
    print(it)