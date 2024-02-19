"""
    filename -> name of file to read
    open() -> default mode is 'r' -> read-only
    file:read method -> reads the entire content of the file
"""
def read_text(filename):
    with open(filename) as current_file:
        print(current_file.read())

"""
    filename -> name of file to open
    open() -> default mode 'r'
    file:readlines() method -> to get all the lines of the file in a list
    file:readline() method -> read/move the buffer to the next line
"""
def read_txt_by_line(filename):
    with open(filename) as current_file:
        lines = current_file.readlines()
        for line in lines:
            print(line, end='')
            line = current_file.readline()

"""
    filename -> name of file to write
    new_text -> new text to write to file
    open(fn,'w') -> opens file in write mode; if file doesn't exist create
    encoding='utf-8' -> standard english characters
    file:write method -> this will overwrite all previous content in existing file
"""
def write_new_txt(filename, new_txt):
    with open(filename, 'w', encoding='utf-8') as current_file:
        current_file.write(new_txt)

"""
    filename -> name of file to append to
    append_text -> new text to append to file
    open(fn,'a') -> opens file in append mode; if file doesn't exist create
    encoding='utf-8' -> standard english characters
    file:write method -> this will append to file; '\n' adds new line
"""
def append_line_txt(filename, append_text):
    with open(filename, 'a', encoding='utf-8') as current_file:
        current_file.write('\n')
        current_file.write(append_text)

#read_text('./files_to_read/backup.py')
#read_txt_by_line('./files_to_read/backup.py')
#write_new_txt('./files_to_read/example.txt', 'this is a test...') 
#append_line_txt('./files_to_read/example.txt', 'this is an extra line')