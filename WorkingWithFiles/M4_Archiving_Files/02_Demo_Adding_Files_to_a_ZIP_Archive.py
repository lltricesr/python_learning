import zipfile

to_add = ['files/01_file.csv', 'files/01_file.txt']

def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:                 #archive -> reference to zipfile
        for current_file in files:                              #loop through file list
            lst = archive.namelist()                            #access list of files already in zip file
            if not current_file in lst:                         #test if file already in zip file
                archive.write(current_file)                     #if not, write current file to zip
            else:
                print(f'File exist in zip: {current_file}')     #if, no write just print

add_to_zip('./files.zip', to_add, 'a')                          #'a' -> opens the zip in append mode