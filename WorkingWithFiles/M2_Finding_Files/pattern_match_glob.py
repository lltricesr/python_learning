from pathlib import Path    #import the Path class


def glob_match(fldr, search):
    p = Path(fldr)
    for current_file in p.glob(search):     #no need to list the files and then search; global search for all files -> return results in a list
        print(current_file)

glob_match('./files', '*2*.t*')
print('-' * 20)
glob_match('./files/subfolder', '*_file_*.t*')
print('-' * 20)
