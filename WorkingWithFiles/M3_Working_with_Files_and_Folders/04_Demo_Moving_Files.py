import shutil

def mv_files(src, dst):
    shutil.move(src, dst)

#mv_files('./files/text.txt', './files/subfolder/text.txt')
#mv_files('./files','./xyz')     #renaming folder
#mv_files('./xyz','./files')    #return to original state