from functionality import *

# register('filo2', 'filoEssam@example.com', 'password123')
# login(email,password)


user = start()

if user != None:
    Home(user)
else:
    print("Mohra 5n2tny")

'''
Pickle is a standard Python module that allows you to 

serialize and deserialize Python objects. 

Serialization is the process of converting an object in memory to a byte stream 
that can be stored on disk or transmitted over a network, 

and deserialization is the reverse process of recreating the 
original object from the byte stream.

The advantages of using pickle are:

Easy to use: Pickle provides a simple interface for serializing and deserializing 
Python objects, which makes it easy to use.

Supports complex objects: Pickle can handle almost any type of Python object, 
including user-defined classes, functions, and instances.

Efficient: Pickle is efficient in terms of both time and space. 
It uses a binary format that is more compact than a text-based format like JSON or XML.

Cross-language support: Since pickle is a standard Python module, 
it can be used to serialize and deserialize Python objects across different 
platforms and programming languages that have pickle libraries.

Preserves object relationships: 
Pickle maintains the relationships between objects in the serialized data, 
so when the data is deserialized, the objects are created with the same relationships 
as in the original program. This is especially useful for complex data structures.

'''
