#!/usr/bin/python3
""" Base class module """

from datetime import datetime
import uuid


class BaseModel():
    """ Base class """

    def __init__(self):
        """ initialize an instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ save this instance """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary of this instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """ String representation of this instance """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))
