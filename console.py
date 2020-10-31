#!/usr/bin/python3
""" Command interpreter """

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
