#This is the interface containing the abstract method for all car objects to implement
#cars are accessed through the Serviceable interface

from abc import ABC, abstractmethod
class Serviceable(ABC):
    @abtsractmethod
    def needs_service(self): #returns bool
        pass

