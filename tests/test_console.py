#!/usr/bin/env python3
"""
===============================================================================
████████╗███████╗███████╗████████╗     ██████╗ █████╗ ███████╗███████╗███████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
   ██║   █████╗  ███████╗   ██║       ██║     ███████║███████╗█████╗  ███████╗
   ██║   ██╔══╝  ╚════██║   ██║       ██║     ██╔══██║╚════██║██╔══╝  ╚════██║
   ██║   ███████╗███████║   ██║       ╚██████╗██║  ██║███████║███████╗███████║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
===============================================================================
"""

import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestConsole(unittest.TestCase):
    """test prompting of the command interpreter"""

    all_classes_name = ["BaseModel", "User", "State", "City", "Amenity",
                        "Place", "Review"]
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

# ******************************************
# help
# ******************************************

    def test_help_quit(self):
        help = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_EOF(self):
        help = "End Of File command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_create(self):
        help = ("Creates a new instance of BaseModel "
                "saves it (to the JSON file) and prints the id.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_all(self):
        help = ("Prints all string representation of all instances\n        "
                "based or not on the class name.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_show(self):
        help = ("Prints the string representation of an instance,"
                " format:\n        "
                "show <class name> <id>.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_destroy(self):
        help = ("Deletes an instance based on the class name and id.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_count(self):
        help = ("counts the number of instances of a class")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_update(self):
        help = ("Updates an instance based on the class"
                " name and id by adding or\n        "
                "updating attribute (save the change into the JSON file).")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help(self):
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, f.getvalue().strip())

    def test_cmd(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

# ******************************************
# console commands
# ******************************************
    def test_create(self):
        """Tests if the create command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                self.assertTrue(i + "." +
                                id_val in storage._FileStorage__objects.keys())

    def test_show(self):
        """Tests if the show command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("show" + " " + i + " " + id_val)
                str_obj = f.getvalue().strip()
                self.assertEqual(str(storage._FileStorage__objects
                                            .get(i + "." + id_val)), str_obj)

    def test_destroy(self):
        """Tests if the destroy command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                self.assertTrue(i + "."
                                  + id_val in storage
                                ._FileStorage__objects.keys())
                HBNBCommand().onecmd("destroy" + " " + i + " " + id_val)
                self.assertTrue(i + "."
                                  + id_val not in storage
                                .all().keys())

    def test_all(self):
        """Tests if the all command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                HBNBCommand().onecmd("create" + " " + i)
            f.truncate(0)
            f.seek(0)
            lst_all = []
            for key in storage._FileStorage__objects.keys():
                lst_all.append(str(storage._FileStorage__objects[key]))
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), str(lst_all))

    def test_count(self):
        """Tests if the count command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                HBNBCommand().onecmd("create" + " " + i)
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("count" + " " + i)
                count = f.getvalue().strip()
                count_expected = 0
                for value in storage._FileStorage__objects.values():
                    if isinstance(value, TestConsole.all_classes[i]):
                        count_expected += 1
                self.assertEqual(int(count), count_expected)


if __name__ == "__main__":
    unittest.main()
