"""
This library demonstrates the functions for creating a generator
"""
def generator246():
    print('Generator is called -')
    yield 2
    print('Generator is called --')
    yield 4
    print('Generator is called ---')
    yield 6


if __name__ == '__main__':
    i=generator246()
    j=generator246()
    print(i)
    print(j)
    m=i.__next__()
    n=i.__next__()
    o=i.__next__()
    print(m,n,o)

    print('-Evaluating through j-',next(j),next(j),next(j))