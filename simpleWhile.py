"""
This is a simple program to demonstarte the while loop in Python
"""
def create_pyramid(height):
    i=1
    while(i<=height):
        i=i+1
        print('i is',i)
        if i == 4:
            #continue
            pass
        print('+'*i)
        print('*'*i)

if __name__ == '__main__':
    create_pyramid(5)

