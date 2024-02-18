#traverse a folder
import os

def traverse(fldr):
    #loop through: folder paths, directories & files returned in the os.walk() for specified fldr
    for fldrpath, dirs, fls in os.walk(fldr):       #walks or traverse all the objects in 1 shot
        print(f'Folder: {fldrpath}')                #sub folder
        for current_file in fls:                    #iterate through the files
            print(f'\t{current_file}')              #print -> tab:file anme

traverse('./files')