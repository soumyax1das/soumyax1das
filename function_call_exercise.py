#!/usr/bin/env python3
"""
This library has functions with different type of function calls.
"""
def banner(message='%',banner_char='-'):
    """
    This function accepts a message and prints it in between banner lines.
    """
    banner_msg=banner_char * len(message)
    print(banner_msg)
    print(message)
    print(banner_msg)

def banner_no_default(message,banner_char):
    """
    This function doesn't have default values, but it can be called with keyword as well as positional parameters.
    :param message:
    :param banner_char:
    :return:
    """
    banner_msg=banner_char * len(message)
    print(banner_msg)
    print(message)
    print(banner_msg)

if __name__ == '__main__':
    #Calls as positional parameters
    banner('Soumya')
    banner('Soumya Das','*')
    #Calls as a combination of positional and keyword parameter
    banner('Lionel Messi',banner_char='#')
    #Calls as fully keyword parameters
    banner(banner_char='$',message='Aarush Das')
    #Calls with default values
    banner()

    #Calls with Keyword parameters
    banner_no_default(banner_char='*',message='Soumya Aarush')
    #Calls with Positional parameters
    banner_no_default('Paramita Pal',':')