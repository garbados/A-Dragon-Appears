from attributes import *

class Entity(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)
                
    def __setattr__(self, name, value):
        if hasattr(self, name) and isinstance(self.name, Attribute):
            self.name.value = value
            
    def __getattr__(self, name):
        if hasattr(self, name) and isinstance(self.name, Attribute):
            return self.name.value
