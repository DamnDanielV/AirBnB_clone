#!/usr/bin/python3
""" Command interpreter """

import cmd
import models
from models.base_model import BaseModel
storage = models.storage

class HBNBCommand(cmd.Cmd):
    """ Command interpreter """

    def __init__(self):
        """ Instatiation for class HBNB """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '


    def do_quit(self, line):
        """ Quit command to exit the program """
        return True


    def do_EOF(self, line):
        """ Signal to interrupt a file """
        return True

    def do_create(self, args):
        """reads a line from command prompt and create an instance"""

        dict_class = {'BaseModel': BaseModel}

        if args == '':
            print('** class name missing **')
        
        elif args != 'BaseModel':
            print("** class doesn't exist **")

        else:
            for key, value in dict_class.items():
                if key == args:
                    object_d = value()
                    object_d.save()
                    print(object_d.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
