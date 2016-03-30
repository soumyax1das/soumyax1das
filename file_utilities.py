"""
This is a library of functions for Uploading save files to Artifactory, using REST API.
"""
import os
import sys
import shutil
import tarfile

def check_file(fileObj):
    """
    This function checks if the input object is an existing file or not.
    :param fileObj: File Name with complete location.
    :return: Returns True if the input is an existing file, otherwise returns False.
    """
    if os.path.isfile(fileObj)==True:
        return(True)
    else:
        return(False)

def check_dir(dirObj):
    """
    This function checks if the input object is an existing directory or not.
    :param fileObj: Directory Name with complete location.
    :return: Returns True if the input is an existing directory, otherwise returns False.
    """
    if os.path.isdir(dirObj)==True:
        return(True)
    else:
        return(False)

def build_dir_for_qa(basedir,dirname,file_list):
    """
    This function creates a directory with save files and corresponding info files.
    :param basedir: Base directory under which target directory will be created.
    :param dirname: Target directory name, this will hold the files.
    :param file_list: This is a list object which should be copied to target directory.
    :return: Returns True, if the directory is created with required objects.
    """
    try:
        for f in file_list:
            if os.path.isfile(f) == False:
                print('{} is not a valid file'.format(f))
                return(False)
        if os.path.isdir(basedir)==False:
            return(False)
        target_dir=basedir+'/'+dirname
        os.mkdir(target_dir)

        for f in file_list:
            shutil.move(f,target_dir)

        return(True)
    except FileExistsError as feE:
        print('File/Directory exists')
        raise
        return(False)
    except PermissionError as prmE:
        print('Permission error occurred')
        raise
        return(False)
    except:
        print('Error not handled, please report to support.')
        raise
        return(False)


def tar_gzip_directory(dirName):
    """
    This function tars a directory and then compresses it with gzip.
    :param dirName: Directory name to be compressed.
    :return: Returns True if tar and compress are successful. Otherwise, returns False.
    """
    try:
        if os.path.isdir(dirName)==True:
            os.chdir(dirName+'/..')
            final_dir=dirName.split('/')[-1]
            out=tarfile.open(final_dir+'.tar.gz',mode='w:gz')
            out.type=tarfile.DIRTYPE
            out.add(final_dir)
            out.close()
            return(True)
        else:
            return(False)
    except:
        raise


if __name__=='__main__':
    #to_Env_var=dict{}
    #to_Env_var[]
    val=check_file('/Users/Aarush/test.dat')
    print(val)
    val=check_dir('/Users/Aarush')
    print(val)
    val=build_dir_for_qa('/Users/Aarush/qa_to','qa_dir',['/Users/Aarush/test.dat'])
    print(val)
    tar_status=tar_gzip_directory('/Users/Aarush/qa_to/qa_dir')
    print(tar_status)