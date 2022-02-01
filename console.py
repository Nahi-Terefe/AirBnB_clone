#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
import cmd
import re


my_classes = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """-HBNBCommand(cmd.Cmd) is a class that inherits from cmd.Cmd
                    cmd.Cmd is methods to execute a command prompt command
                    line interface for a Python program.
       -prompt is a interpreter-specific string that is displayed to the user
       when they are ready to enter a command.
       -classes is a list of all the classes that inherit from BaseModel.
       -my_objects is a dictionary of all the instances of the classes
       in classes.
       -my_classes oa dictionary whit the classes.
       -storage is an instance of FileStorage.
       -self is an instance of HBNBCommand to use the methods of the class.
       -args is a list of arguments passed to the command.
       -args_list is a list of arguments passed to the command."""

    prompt = "(hbnb) "
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    all_commands = ['create', 'show', 'destroy', 'all', 'update', 'count']

    error_occurred = False

    def precmd(self, line):
        """Manipulate the user input before getting processed."""
        if '{' in line and '}' in line:
            args = re.findall(r"([^(,):{}]+)", line)
            args = [x.strip() for x in args]
            args[:] = [x for x in args if x]
            class_name = args[0].split('.')[0]
            cmd_name = args[0].split('.')[1]
            id_val = args[1].strip("'")
            del args[0]
            del args[0]
            print(args)
            j = 0
            for i in range(len(args) // 2):
                loop_line = ""
                key = args[j].strip("'")
                value = args[j + 1].strip("'")
                loop_line = cmd_name + " " + class_name + " "\
                                     + id_val.strip('"') + " "\
                                     + key.strip('"') + " "\
                                     + value
                j += 2
                cmd.Cmd.onecmd(self, loop_line)
                if HBNBCommand.error_occured:
                    break
            line = ""

        elif '.' in line and '(' in line and ')' in line:
            args = re.findall(r"([^(,):{}]+)", line)
            args = [x.strip() for x in args]
            args[:] = [x for x in args if x]
            class_name = args[0].split('.')[0]
            cmd_name = args[0].split('.')[1]
            if cmd_name not in HBNBCommand.all_commands:
                line = cmd_name
            elif len(args) > 1:
                id_val = args[1].strip('"')
                del args[0]
                del args[0]
                line = cmd_name + " " + class_name + " " + id_val
                for i in args:
                    line = line + " " + i
            else:
                line = cmd_name + " " + class_name
        return line

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        quit()

    def do_EOF(self, args):
        """End Of File command to exit the program"""
        quit()

    def emptyline(self):
        """Do nothing on empty line\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel \
saves it (to the JSON file) and prints the id.
        """
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        else:
            if args[0] in HBNBCommand.all_classes.keys():
                obj = HBNBCommand.all_classes[args[0]]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance, format:
        show <class name> <id>."""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key_obj = args[0] + "." + args[1]
            try:
                print(str(storage._FileStorage__objects[key_obj]))
            except KeyError:
                print('** no instance found **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key_obj = args[0] + "." + args[1]
            try:
                del storage._FileStorage__objects[key_obj]
                storage.save()
            except KeyError:
                print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        args = arg.split()
        if len(args) < 1:
            lst_all = []
            for key in storage._FileStorage__objects.keys():
                lst_all.append(str(storage._FileStorage__objects[key]))
            print(lst_all)
        else:
            if args[0] not in HBNBCommand.all_classes.keys():
                print("** class doesn't exist **")
            else:
                lst_all = []
                for key in storage._FileStorage__objects.keys():
                    if key.split('.')[0] == args[0]:
                        lst_all.append(str(storage._FileStorage__objects[key]))
                print(lst_all)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        HBNBCommand.error_occurred = False
        args = re.findall(r'[^\"\s]\S*|\".+?\"', arg)
        if len(args) < 1:
            print('** class name missing **')
            HBNBCommand.error_occurred = True
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            HBNBCommand.error_occurred = True
        elif len(args) < 2:
            print('** instance id missing **')
            HBNBCommand.error_occurred = True
        elif (args[0] + "." + args[1]) not in\
                storage._FileStorage__objects.keys():
            print('** no instance found **')
            HBNBCommand.error_occurred = True
        elif len(args) < 3:
            print('** attribute name missing **')
            HBNBCommand.error_occurred = True
        elif len(args) < 4:
            print('** value missing **')
            HBNBCommand.error_occurred = True
        else:
            key_obj = args[0] + "." + args[1]
            selected_obj = storage._FileStorage__objects[key_obj]
            selected_obj_dict = selected_obj.to_dict()
            if '"' not in args[3] and "'" not in args[3]:
                if args[3].isdigit():
                    value = int(args[3])
                else:
                    value = float(args[3])
            else:
                value = args[3].strip('"')
            selected_obj_dict.update({args[2].strip('"'): value})
            updated_obj = HBNBCommand.all_classes[args[0]](**selected_obj_dict)
            storage._FileStorage__objects.update({key_obj: updated_obj})
            updated_obj.save()

    def do_count(self, arg):
        """counts the number of instances of a class"""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        else:
            if args[0] in HBNBCommand.all_classes.keys():
                count = 0
                for obj in storage._FileStorage__objects.values():
                    if isinstance(obj, HBNBCommand.all_classes[args[0]]):
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
