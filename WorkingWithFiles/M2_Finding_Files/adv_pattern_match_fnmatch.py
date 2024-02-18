import os, fnmatch  #import the fnmatch module

def match(fldr, search):
    for current_file in os.listdir(fldr):
        if fnmatch.fnmatch(current_file,search):        #allows the use of wildcards
            print(current_file)

match('./files', '*_file*.*')   #any string -> _file -> any string substring with any extension. 
print('-' * 20)
match('./files', '*_file_*.*')   #any string -> _file_ -> any string substring with any extension. 
print('-' * 20)
match('./files', '*2_*_*.*')   #any string -> 2_ -> any string_ -> any substring with any extension. 
print('-' * 20)
