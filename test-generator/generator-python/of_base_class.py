'''
This is the base class for all output formatters. 
The send method is abstract and must be supplied by any subclasses.
'''
from abc import ABC, abstractmethod

class OutputFormatterBaseClass(ABC):
    def __init__(self, name=None):
        self.name = name
        super(OutputFormatterBaseClass, self).__init__()

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def close(self):
        pass