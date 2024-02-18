import os 

def remove_file(del_file):
    if os.path.isfile(del_file):                            #check if a file object
        try:                                                #using try except block as OS operation could cause error
            os.remove(del_file)                             #use remove method on object to delete
        except OSError as e:                                #catch the OS error if 1 occurs
            print(f'Error: {del_file} : {e.strerror}')      #print error
    else:                                                   #if not a file then print error message
        print(f'Error: {del_file} is not a valid file')

remove_file('./files/text.txt')