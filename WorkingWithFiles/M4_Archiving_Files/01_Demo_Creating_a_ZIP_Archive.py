#archive is a collection of compressed files
#zip file is the most common; zip and archive file used interchangeably
import zipfile  #import zipfile module

fldr_path = './files/'
sub_fldr_path = './files/subfolder/'

to_zip = [
    f'{sub_fldr_path}01_file_test.csv',
    f'{sub_fldr_path}01_file_test.txt',
    f'{sub_fldr_path}01_test_file.csv',
    f'{sub_fldr_path}01_test_file.txt',
    f'{fldr_path}01_file_test.csv',
    f'{fldr_path}01_file_test.txt'
]
#print(to_zip)

"""
    zipf -> name of zipfile
    files -> list fo files to zip
    opt -> zip file options
"""
def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf,opt,allowZip64=True) as archive:      #allowZip64=True means are zip can be many MB in size
        for current_file in files:          #loop through files
            archive.write(current_file)     #write the current file to the archive with the write method

create_zip('./files.zip', to_zip, 'w')      #'w' -> open zip file in write mode
