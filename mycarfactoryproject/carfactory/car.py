from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery
    
    """
    Rather than using a convoluted inheritance
    hierarchy, each car is a composition of different
    parts - when needs_service() is called, the Car
    object calls needs_service() on each of its parts
    and returns true if any of them return true
    """
    def needs_service(self):
    	return self.battery.needs_service() or self.engine.needs_service()
    	

