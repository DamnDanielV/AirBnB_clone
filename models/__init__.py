#!/usr/bin/python3
""" Creates a unique instance"""

from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
