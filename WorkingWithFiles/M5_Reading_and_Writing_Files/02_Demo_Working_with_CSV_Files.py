import csv

"""
    filename -> name of file to read
    delimiter -> delimter of the columns in the csv file (which are commas)
    open() -> default 'r' -> read
    cnt -> counter initilized:-1; -1 will print the headers of the csv file .join() by | for the list; used to diff header from data rows
    csv:reader -> returns a reader (as rows in the file), separated by the delimiter
    row[] -> each row is split by delimiter as a list; each element in list is a column; based zero
"""
def read_csv(filename, delimiter):
    with open(filename) as csv_file:
        cnt = -1
        rows = csv.reader(csv_file, delimiter=delimiter)
        for row in rows:
            if cnt == -1:
                print(f'{" | ".join(row)}')
            else:
                print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
            cnt += 1
        print(f'{cnt} lines')

"""
    filename -> name of file to write to
    header -> file header
    row -> data row
    open(mode='w', newline='') -> open in write; newline are started with
    csv:writer -> method return a writer object for csv files
    quotechar='"' -> in case a data element contains any quotes
    quoting=csv.QUOTE_MINIMAL -> tells writer to keep quotes to bare minimum
    writer:writerow -> writes the entire row to the file
"""
def write_csv(filename, header, row):
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)


#read_csv('./files_to_read/names.csv', ',')
"""
    name of csv
    header in array
    data in array -> same # of header array
"""
"""
write_csv(
    './files_to_read/names2.csv',
    ['name', 'lastname', 'age', 'sex'],
    ['Foo', 'Fighter', '82', 'male']
)
"""
read_csv('./files_to_read/names2.csv', ',')