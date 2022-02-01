#!/usr/bin/env python3
"""
AirBnB console module    
"""

import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ HBNB Command class """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}
    
        
    def do_quit(self, args):
        """ Quit command to exit the program """
        quit()

    def do_EOF(self, args):
        """ Exit command to exit the program when EOF """
        quit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass
    
    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ 
        Prints the string representation of an instance based
        on the class name and id 
        """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ 
        Deletes an instance based on the class name and id
        and save the change into the JSON file 
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute and save the change into the JSON file
        """
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

    def do_count(self, args):
        """Counts the number of instances of a certain class"""
        counter = 0
        my_objects = models.storage.all()
        """my_objects is a dictionary with the key and value of the
             dictionary"""
        if args in self.classes:
            for key in my_objects.keys():
                """for key in my_objects.keys() is a loop that
                iterates over the keys of the dictionary"""
                find_class = key.split(".")
                """find_class is a list of the key split by "." """
                if find_class[0] == args:
                    """if find_class[0] == args, then the class name
                    is the same as the args"""
                    counter += 1
                    """counter += 1 is a function that adds 1 to the counter"""
            print(counter)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
