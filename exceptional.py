import sys
def convert(i):
    try:
        x=int(i)
        print('Value is -',x)
    except (ValueError,TypeError) as e:
        print('Conversion failed')
        print(str(e))
        #raise

    except (IndentationError, SyntaxError, NameError):
        pass

if __name__ == '__main__':
    convert(3)
    convert('a')
    convert(6)

