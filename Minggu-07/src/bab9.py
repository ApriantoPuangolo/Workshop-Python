def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

  x = MyClass()

kind = 'canine'         # class variable shared by all instances

def __init__(self, name):
    self.name = name    # instance variable unique to each instance

tricks = []             # mistaken use of a class variable

def __init__(self, name):
    self.name = name

def add_trick(self, trick):
    self.tricks.append(trick)

def __init__(self, name):
    self.name = name
    self.tricks = []    # creates a new empty list for each dog

def add_trick(self, trick):
    self.tricks.append(trick)

