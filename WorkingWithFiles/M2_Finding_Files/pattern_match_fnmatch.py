import os, fnmatch  #import the fnmatch module

def match(fldr, search):
    for current_file in os.listdir(fldr):
        if fnmatch.fnmatch(current_file,search):        #allows the use of wildcards
            print(current_file)

match('./files', '*.csv')
print('-' * 20)
match('./files', '*_file.csv')
print('-' * 20)
match('./files', '*1*_file.csv')
print('-' * 20)
match('./files', '*2*_file.csv')
print('-' * 20)
match('./files', '*2*_test.csv')
print('-' * 20)
