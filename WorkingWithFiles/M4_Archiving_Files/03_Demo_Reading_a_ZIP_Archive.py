import zipfile

def read_zip(zipf):
    with zipfile.ZipFile(zipf,'r') as archive:              #'r' -> read-only mode for zip
        lst = archive.namelist()                            #retreive the list of files in the zip
        for current_file in lst:                            #loop through list
            zfinfo = archive.getinfo(current_file)          #retreive the info/attributes about the file in the zip
            #print the current file name, size in bytes, and compressed size
            print(f'{current_file} => {zfinfo.file_size} bytes, {zfinfo.compress_size} compressed')

read_zip('./files.zip')