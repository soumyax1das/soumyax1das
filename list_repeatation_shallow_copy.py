#/usr/bin/env python3
"""
This is to demonstrate list repeatation and show that the repeatation is a shallow copy
Author :: Soumya Das
"""
def repeat_list_then_modify(lst, rep_factor):
    """
    This is a shallow copy
    :param lst:
    :param rep_factor:
    :return:
    """
    final_lst=lst * rep_factor
    print(final_lst)
    final_lst[0].append(99)
    print(final_lst)
    print(final_lst[0])
    print(id(final_lst[0]))
    print(final_lst[2])
    print(id(final_lst[2]))
    final_lst[0][0]=33
    print(final_lst[0])
    print(final_lst[2])
    print(id(final_lst[0]))
    print(id(final_lst[2]))


def repeat_1d_list_then_modify(lst, rep_factor):
    """
    This is not a shallow copy
    :param lst:
    :param rep_factor:
    :return:
    """
    final_lst=lst * rep_factor
    print(final_lst)

    final_lst[0]=999

    print(final_lst)
    print(final_lst[0])
    print(id(final_lst[0]))
    print(final_lst[4])
    print(id(final_lst[2]))


if __name__ == '__main__':
    l=[[1,2,3,4],[4,5,6,7]]
    repeat_list_then_modify(l,3)

    l=[6,7,8,9]
    repeat_1d_list_then_modify(l,3)
