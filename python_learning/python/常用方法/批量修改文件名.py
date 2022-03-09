import os


def create_files():
    os.chdir('new_dir')
    for i in range(10):
        file_name = "test_" + str(i) + '.txt'
        f = open(file_name, 'w')
        f.close()
    os.chdir('../')


def before_rename_files():
    os.chdir('new_dir')
    file_list = os.listdir()
    for file_name in file_list:
        new_file = 'py' + file_name
        os.rename(file_name, new_file)
    os.chdir('../')


# 改掉pytest
def sub_rename_files():
    os.chdir('new_dir')
    file_list = os.listdir()
    for file_name in file_list:
        num = len('pytest')
        new_file = 'py' + file_name[num:]
        os.rename(file_name, new_file)
    os.chdir('../')


# create_files()
# before_rename_files()
# sub_rename_files()
