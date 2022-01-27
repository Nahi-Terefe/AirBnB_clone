#!/usr/bin/python3
"""
    console module    
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB Command class """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}
    
        
    def do_quit(self, arg):
            """ Quit command to exit the program """
            exit()

    def do_EOF(self, arg):
        """ Exit command to exit when EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()