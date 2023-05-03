#import the  CarFactory class from the carfactory package
from carfactory import CarFactory
#import the Car class from the car.py module
from car import Car
#import the date
from datetime import date
 



#create class 
class CalliopeFactory(CarFactory):
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return car(calliope,) #return a car model calliope