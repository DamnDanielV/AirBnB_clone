# AirBnB clone project!

## Description

The AirBnb_clone Project is the part number 1 of a series of projecs we will do in our process to become Full-Stack Software Engineers. This first phase consists in a custom command-line interface that allow us to create, update an delete instances of different classes. Also, AirBnB project has a storage class and a BaseModel class that allows the console do its work.

## Usage

The console works in interactive an non-interactive mode, like unix shell. It prints the prompt (hbnb) and waits an instruction:

The folder engine manages the serialization adn deserialization of all data. The class is defined in file_storage.py with methods to follow this: -> to_dict() -> -> JSON dump -> -> FILE -> -> JSON load -> ->

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

# Tests

All the code is tested with the unittest module.