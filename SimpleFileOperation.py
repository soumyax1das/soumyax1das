"""
    This program demonstates simple file operations using Python.
    Author :: Soumya Das
"""
def create_sample_files(file_loc, fmode,fencode):
    """
    This function takes file location and mode and
    :param file_loc:
    :return:
    """
    #f=open(file_loc,mode=fmode,encoding=fencode)
    f=open(file_loc,mode='wt',encoding=fencode)
    f.write('This file is written through Python')
    f.close()
    f=open(file_loc,mode='r')
    str=f.readline()
    print(str)
    f.close()



if __name__ == '__main__':
    create_sample_files('/Users/Aarush/sample_file.dat','wt','utf-8')