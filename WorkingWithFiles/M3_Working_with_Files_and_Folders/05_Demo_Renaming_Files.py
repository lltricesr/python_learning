import os
from pathlib import Path

def rename_file_1(src, dst):
    os.rename(src,dst)          #using the rename method on the os

def rename_file_2(src, dst):
    f = Path(src)               #create a file object from the path
    f.rename(dst)               #useing the rename method on the file object

#rename_file_1('./files/text.txt', './files/test.txt')
rename_file_1('./files/test.txt', './files/text.txt')