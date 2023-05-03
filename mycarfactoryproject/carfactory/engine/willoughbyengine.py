from engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__() 
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self): #returns bool
        return self.current_mileage - self.last_service_mileage > 60000


