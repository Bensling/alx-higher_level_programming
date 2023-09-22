#!/usr/bin/python3
"""Defines base model class."""

import json
import csv
import turtle


class Base:
    """Represents base model.

    Attributes:
        __nb_objects (int): the number of instantiated bases.
    """

    __nd_object = 0

    def __init__(self, id=None):
        """Initializing a new Base.

        Args:
            id (int): identity of new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_objects
