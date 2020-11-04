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

    prompt = '(hbnb) '
    class_l = [
                'BaseModel',
                'User',
                'Place',
                'State',
                'City',
                'Amenity',
                'Review',
                ]

    def emptyline(self):
        print

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Signal to interrupt a file """
        return True

    def do_create(self, *args):
        """reads a line from command prompt and create an instance"""
        args = [e for e in args[0].split(' ')]
        if args[0] == '':
            print('** class name missing **')
            return
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return
        else:
            object_d = eval('{}()'.format(args[0]))
            object_d.save()
            print(object_d.id)

    def do_show(self, *args):
        """ Prints the string representation of
        an instance based on the class name and id """
        args = [e for e in args[0].split(' ')]
        if args[0] == '':
            print('** class name missing **')
            return
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return

        storage.reload()
        objs_dict = storage.all()

        if objs_dict is None:
            print("** no instance found **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in objs_dict.keys():
            print(objs_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id"""
        args = [e for e in args[0].split(' ')]
        if args[0] == '':
            print('** class name missing **')
            return
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return

        storage.reload()
        objs_dict = storage.all()

        if objs_dict is None:
            print("** no instance found **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in objs_dict.keys():
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, *args):
        """
        Prints all string representation of all instances
        """
        args = [e for e in args[0].split(' ')]
        obj_p = []
        storage.reload()
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return
        elif args[0] == '':
            for key, value in storage.all().items():
                obj_p.append(value.__str__())
            print(obj_p)
            return
        else:
            for key, value in storage.all().items():
                key = key.split('.')
                if key[0] == args[0]:
                    obj_p.append(value.__str__())
            print(obj_p)

    def do_update(self, *args):
        """Updates an instance based on the class
            name and id by adding or updating attribute
        """
        if len(args) == 1:
            args = [e for e in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.class_l:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        storage.reload()
        objs_dict = storage.all()
        if objs_dict is None:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in objs_dict.keys():
            oj = objs_dict[key]
            if args[2] in oj.__class__.__dict__:
                oj.__dict__[args[2]] = type(obj.__class__.
                                            __dict__[args[2]](args[3]))
            else:
                oj.__dict__[args[2]] = args[3]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
