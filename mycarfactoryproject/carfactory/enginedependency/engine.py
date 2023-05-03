#this will be the engine abstract superclass
#inherits the Car class and will let the subclasses implement the abstract class


from carfactory.car import Car

class Engine(Car):
    @abstractmethod
    def needs_service():
        pass


