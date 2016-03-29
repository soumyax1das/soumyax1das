"""
This script explains string partition function.
Partition always returns 3 member tuple, data before partition, partition key itself and the rest.
Author :: Soumya Das
"""

def partition_and_show(str,sep):
    tup=str.partition(sep)
    print(tup)

if __name__ == '__main__':
    partition_and_show('Lionel:Andreas:Messi:Cuccutino',':')