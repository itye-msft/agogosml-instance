'''
This is the base class for all custom tests. 
The generate method is abstract and must be supplied by any subclasses.
'''
from abc import ABC, abstractmethod

class TestBaseClass(ABC):
    def __init__(self, name=None):
        self.name = name
        super(TestBaseClass, self).__init__()

    @abstractmethod
    def generate(self):
        pass
