#JavaScript Object Notation (JSON)
import json

"""
    filename -> name of json file
    pretty -> indicator if we want to return formatted
    sort -> perferred sort
    open() -> default 'r' - read-only
    json:load -> reads in json file and returns object file as data
    data -> load() doesn't return in a user friendly manner; thus pretty boolean
    json:dumps -> returns a str based on the loaded data, sort_keys, & indent
    dumps(data,sort,indent) if pretty else dumps(data) -> ternary notation (if else shorthand)
        Syntax: [on_true] if [expression] else [on_false]
        expression: conditional_expression | lambda_expr
"""
def read_print_json(filename, pretty, sort) -> None:
    with open(filename) as json_file:
        data = json.load(json_file)
        print(json.dumps(data,sort_keys=sort,indent=4))         
        #can't seem to get the ternary to work
        #print(json.dumps(data, sort_keys=sort, indent=4 if pretty else data))

"""
    filename -> name of json file
    authors_arr_name -> name/key to locate the author's array in the json; array of authors
    arr_pos -> the array position of the author to update
    author_dict_key -> which key in the author dict wanting to update; author -> is a dict {'name','course'}
    new_value -> new value to set the author key to
    open(fn,'r') -> open json for read-only
    json:load -> read the json file and load the data
    data -> str representation of the json
    open(fn,'w') -> open json for write
    json:dump -> method to write the data to the json file
"""
def update_author_json(filename, authors_arr_name, arr_pos, author_dict_key, new_val) -> None:
    with open(filename,'r') as read_file:
        data = json.load(read_file)
        data[authors_arr_name][arr_pos][author_dict_key] = new_val
        with open(filename,'w') as write_file:
            json.dump(data, write_file)

#read_print_json('./files_to_read/authors.json', False, False)
"""
update_author_json(
    './files_to_read/authors.json',
    'authors',
    1,
    'courses',
    10
)
"""
