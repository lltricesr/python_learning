import os

#does the file name end with the search criteria
def ends_with(fldr, search):
    for current_file in os.listdir(fldr):
        if current_file.endswith(search):
            print(current_file)

#does the file name start with the search criteria
def starts_with(fldr, search):
    for current_file in os.listdir(fldr):
        if current_file.startswith(search):
            print(current_file)

#ends_with('./files', '.txt')
starts_with('./files', '01_test')