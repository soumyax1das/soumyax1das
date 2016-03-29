"""
This program is a sample for
a) using lambda expressions.
b) Also it shows various scopes of variables in Python - LEGB
    L : Local
    E : Enclosing Function
    G : Global
    B : Built in
c) Also it shows how to change a global variable from within a function
"""


def greet():
    #E: Enclosing function Scope (name)
    name = 'Sammy'

    def hello():
        global surname
        print('Hello-',name)
        print(id(name))

        #Modify a global variable from within a function.
        surname='Das'
        print('---------------')
        locals()
        print('---------------')
        globals()
    hello()

if __name__ == '__main__':
    #G: Global Scope (name)
    name='Soumya'
    surname='Anything'
    print(id(name))
    #L: Local Scope, x is local within the lambda expression.
    sqr = lambda  x:x**2
    print(sqr(2))
    print(surname)
    greet()
    print(surname)
