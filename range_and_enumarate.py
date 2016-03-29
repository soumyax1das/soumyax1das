"""
This is a function example to explain range and enumarate function.
Author::Soumya Das
"""
def range_and_enumarate_example(range_start,range_stop,range_gap):
    ran=range(range_start,range_stop,range_gap)
    for i in ran:
        print(i)

    for i,j in enumerate(ran):
        print(i,j)


if __name__ == '__main__':
    range_and_enumarate_example(9,30,3)


