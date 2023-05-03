from carfactory.car import Car

class Battery(Car):
    @abstractmethod
    def needs_service(self):
        pass


