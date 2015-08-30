#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import inspect
"""
This Module allows you to create classes with typed properties in Python. Some people might think of this as 'unpythonic' but it has its use cases.
For example the age of a person, which has to be int and not str.
Here is a little example:

    from static_typed import *
    
    class Person(Model):    # subclass Model to get Constructor and __repr__
        name    = Type(str)
        age     = Type(int, 0) # default 0
        married = Type(bool, False)
        __cons__= ['name', 'age', 'married']   # specify this to use constructor without named arguments

    mary = Person("Mary", 25, married=True)
    print(mary.age) # 25
    mary.age = "26" # does: mary.age = int("26")
    print(mary.age) # 26


"""

class Type(object):
    """
    Specifies of which type the property has to be
    """

    def __init__(self, typ, default=None):
        self.value = default
        self.type = typ

    def __get__(self, _, value):
        return self.value

    def __set__(self, _, value):
        if value:
            self.value = self.type(value)

class Model(object):
    """
    Subclass this to get an automagically generated __init__ method and pretty printing through __repr__
    """
    def __init__(self, *args, **kwargs):
        for key, val in zip(self.__cons__, args):
            setattr(self, key, val)
        
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def _members(self):
        all_props = inspect.getmembers(self.__class__, lambda m: not inspect.ismethod(m))
        props = []
        for k,v in all_props:
            if not k[0] == '_':
                props.append((k,v))
        return props

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__, 
            ", ".join([
                "{}={}".format(
                    k, 
                    repr(getattr(self, k))) 
                    for k, v in self._members
            ]))

    def __str__(self):
        return repr(self)

