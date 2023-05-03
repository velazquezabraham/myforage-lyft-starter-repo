from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery
""" 
    def get_engine(self):
        return self.__engine

    def get_battery(self):
        return self.__battery
"""
    @abstractmethod
    def needs_service(): #returns bool
        pass


