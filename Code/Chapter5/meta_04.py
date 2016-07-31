#!/usr/bin/env python
# coding: utf-8
#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Metaprogramming.html

class RegisterClasses(type):
    def __init__(cls, name, bases, atts):
        super(RegisterClasses, cls).__init__(name, bases, atts)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        
        cls.registry.add(cls)
        cls.registry -= set(bases) # Remove base classes
    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)
    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])

class Shape(object):
    __metaclass__ = RegisterClasses

class Round(Shape): pass
class Square(Shape): pass
class Triangular(Shape): pass
class Boxy(Shape): pass
print Shape
class Circle(Round): pass
class Ellipse(Round): pass
print Shape

for s in Shape: # Iterate over subclasses
    print s
