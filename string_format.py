"""
This function shows how to use format method in different ways
Author :: Soumya Das
"""
import math
def string_format(str):
    print(str.format('val1','val2','val3'))


def string_format_import_math_library(str):
    print(str.format(m=math))

if __name__ == '__main__':
    string_format('parm1={} parm2={} parm3={}')
    string_format('parm1={1} parm2={0} parm3={2}')
    string_format_import_math_library('Value of PI is {m.pi}')
