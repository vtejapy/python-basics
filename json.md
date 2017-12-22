"JSON (pronounced 'Jason'), short for JavaScript Object Notation, is a lightweight computer data interchange format. It is a text-based, human-readable format for representing simple data structures and associative arrays (called objects)."
JSON can store Lists, bools, numbers, tuples and dictionaries. But to be saved into a file, all these structures must be reduced to strings. It is the string version that can be read or written to a file. Python has a JSON module that will help converting the datastructures to JSON strings. Use the import function to import the JSON module.


Functions
json.dump(obj, fileObj): Serializes obj as a JSON formatted stream to fileObj.
json.dumps(obj) : Serializes obj as JSON formatted string.
json.load(JSONfile) : De-serializes JSONfile to a Python object.
json.loads(JSONfile) : De-serializes JSONfile(type: string) to a Python object.

Classes
JSONEncoder: An encoder class to convert Python objects to JSON format.
JSONDecoder: A decoder class to convert JSON format file into Python obj.

The conversions are based on this conversion table.


import json

The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.

json_string = json.dumps(datastore)

The JSON module can also take a JSON string and convert it back to a dictionary structure:

datastore = json.loads(json_string)

While the JSON module will convert strings to Python datatypes, normally the JSON functions are used to read and write directly from JSON files.


Parsing JSON

Take the following string containing JSON data:

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

It can be parsed like this:

import json
parsed_json = json.loads(json_string)

and can now be used as a normal dictionary:

print(parsed_json['first_name'])
"Guido"

You can also convert the following to JSON:

d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}

print(json.dumps(d))
'{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "De
