#!/usr/bin/python3
"""
File Storage module:
    - serializes instances to a JSON file into storage and
    - deserializes JSON file to instances from storage
"""
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel

class FileStorage():
    """ FilsStorage class """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """ return dictionary objects loaded in __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the dictionary __objects 
            using obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ serializes objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
        """ Reload the file """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                load_json = json.load(fname)
                for key, val in load_json.items():
                    FileStorage.__objects[key] = eval(
                        val['__class__'])(**val)
