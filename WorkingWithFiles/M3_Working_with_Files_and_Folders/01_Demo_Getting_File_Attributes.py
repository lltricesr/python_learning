#getting file attributes for any file
import os
from datetime import datetime, timezone #import datetime and timezone -> used to convert time

#returns the date time stamp in utc time
def get_date(timestmp):     
    # deprected -> return datetime.utcfromtimestamp(timestmp).strftime('%d %b %Y') #day-mon-year
    return datetime.fromtimestamp(timestmp, timezone.utc).strftime('%d %b %Y')  #E.g. 11 Sep 2022

def get_file_attrs(fldr):
    with os.scandir(fldr) as dir:                           #open a directory scan as variable dir
        for current_file in dir:                            #iterate through dir files
            if current_file.is_file():                      #if the current file is a file -> not a subdirectory
                file_attrs = current_file.stat()            #grab all the file attributes
                #print the modified time in utc using get_date function
                print (f'Modified {get_date(file_attrs.st_mtime)} {current_file.name}') 

get_file_attrs('./files/subfolder')