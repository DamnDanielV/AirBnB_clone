#!/usr/bin/python3
""" Command interpreter """

import cmd
import models

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
storage = models.storage


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """

    class_l = [
                'BaseModel',
                'User',
                'Place',
                'State',
                'City',
                'Amenity',
                'Review',
                ]

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
        args = args.split(' ')
        if args == '':
            print('** class name missing **')
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return
        else:

            object_d = eval('{}()'.format(args[0]))
            object_d.save()
            print(object_d.id)

    def do_show(self, args):
        """ Prints the string representation of
        an instance based on the class name and id """

        if args == '':
            print('** class name missing **')

        else:
            args = args.split(' ')
            if args[0] not in self.class_l:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print('** instance id missing **')
                return

        storage.reload()
        objs_dict = storage.all()

        key = "{}.{}".format(args[0], args[1])
        if key in objs_dict.keys():
            print(objs_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        if args == '':
            print('** class name missing **')

        else:
            args = args.split(' ')
            if args[0] not in self.class_l:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print('** instance id missing **')
                return

            objs_dict = storage.all()

            for key in objs_dict.keys():
                if args[1] in key:
                    del objs_dict[key]
                else:
                    print("** no instance found **")
                    return
                storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        """
        args = args.split()
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return

        objs_dict = storage.all()

        for value in objs_dict.values():
            print(value)

    def do_update(self, args):
        """Updates an instance based on the class
            name and id by adding or updating attribute
        """
        if args == '':
            print('** class name missing **')

        else:
            objs_dict = storage.all()
            args = args.split()
            if args[0] not in self.class_l:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print('** instance id missing **')
                return
            for key in objs_dict.keys():
                if args[1] in key:
                    value = args[3].strip('"\'')
                    objs_dict[key].update(args[2], value)
                else:
                    print("** no instance found **")
                    return

            if len(args) < 3:
                print('** attribute name missing **')
                return
            elif len(args) < 4:
                print('** value missing **')
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
