#inherits the Engine class to implement its abstract method

from engine import Engine

class CapuletEngine(Engine):
    def __init__(self,last_service_mileage, current_mileage):
        super().__init__()#call to superclass init ctor
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self): #returns bool true if current > last
        return self.current_mileage - self.last_service_mileage > 30000



