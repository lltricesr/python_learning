import shutil       #import the shutil -> shell utility

def copy_file(src, dst):        #src -> source file to copy; dst -> destination folder to add file
    shutil.copy(src,dst)        #copy method in shutil to copy files

def copy_folder(src, dst):      #src -> source folder to copy; dst -> destination folder to add folder
    shutil.copytree(src,dst)    #copytree method in shutil to copy folders

#copy_file('./files/02_file.txt', './files/subfolder')
#copy_folder('./files', './files/new_fldr')
copy_file('./files/subfolder/text.txt', './files/text.txt')