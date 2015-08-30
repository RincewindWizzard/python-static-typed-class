# Static typed members for python classes
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
