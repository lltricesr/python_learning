"""
    persist into binary file
    saving internal state to disk, a db or over the network
    importing pickle module
        pickle is used to serialize a python class and its value for storage in binary file
"""
import pickle

"""
    Sample Person Class to instantiate for demonstration
"""
class Person:
    age = 45
    name = 'John Smith'
    kids = ['Pete', 'Lilly', 'Kate']
    employers = {'AWS':2022, 'Microsoft':2018,'Yahoo': 2005}
    shoe_sizes = (11,12)
"""
    py_obj -> the python obj (instantiated class w/ state) that is being serialized for storage
    pickle:dumps -> converts python obj and returns binary obj (bytes) based on the defined serialization protocol
    pickled -> serialized binary obj in bytes
"""
def serialize(py_obj):
    pickled = pickle.dumps(py_obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: \n{pickled}\n')
    return pickled

"""
    bin_obj -> binary obj that is being deserialized into a python obj (Person)
    pickle:loads -> method to convert the binary obj to python obj
"""
def deserialize(bin_obj):
    unpickled = pickle.loads(bin_obj)
    print(f'Deserialized: \n{unpickled}\n')

"""
    bin_obj -> binary obj of the python obj (Person)
    pickle:loads -> method to convert the binary obj to python obj
    unpickled:employers -> attribute of the person obj representing the employers dict
"""
def deserialize_employers(bin_obj):
    unpickled = pickle.loads(bin_obj)
    print(f'Deserialized employers: \n{unpickled.employers}\n')

"""
    filename -> file name to save (persist) the binary obj
    bin_obj -> binary obj to persist to file
    open(fn,'wb') -> opens file in write binary mode
    pickle:dump -> write the binary obj to the persistance file using the binary protocol
"""
def obj_to_file(filename, bin_obj):
    with open(filename,'wb') as persist_file:
        pickle.dump(bin_obj,persist_file,protocol=pickle.HIGHEST_PROTOCOL)

"""
    filename -> file to read binary obj
    py_obj -> instance of the python obj (Person)
    open(fn,'rb') -> opens file in read binary mode
    pickle:load -> reads the binary obj from the persistance file, returns python obj
"""
def file_to_obj(filename, py_obj):
    with open(filename,'rb') as persist_file:
        py_obj = pickle.load(persist_file)
        print(py_obj)
        return py_obj

# 2/28 - unclear about this as func doesn't have a return
obj = obj_to_file('./files_to_read/person.xyz', Person())
print(obj)
person = file_to_obj('./files_to_read/person.xyz', obj)
"""
pickled = serialize(Person())       #create a binary obj from Person
deserialize(pickled)                #deserialize binary obj
deserialize_employers(pickled)      #deserialize employers from the binary obj
"""