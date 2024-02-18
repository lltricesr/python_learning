import os   #import the os modules for accessing system folders

#func to list a director
def list_dir(fldr):
    #loop through all the files in folder; all objects {file, folder} in a directory list are files by default
    for current_file in os.listdir(fldr):
        #print the name of the file
        print(current_file)

#call the function
list_dir('./files')