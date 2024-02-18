import zipfile

"""
    zipf -> name of the existing zip file
    fn -> file name to extract
    path -> location to extract file to
"""
def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn,path)                #extract 1 file

"""
    zipf -> name of the existing zip file
    path -> location to extract all the files to
"""
def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path)                #extract all files

#extract_file('./files.zip', 'files/01_file_test.txt', 'extracted')
#extract_all('./files.zip', 'extracted')