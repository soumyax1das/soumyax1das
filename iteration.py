def do_iteration(iterable):
    iterator=iter(iterable)
    try:
        while(1==1):
            print(next(iterator))


    except(StopIteration)as e:
        print(str(e))
        raise


if __name__ == '__main__':
    s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    do_iteration(s)