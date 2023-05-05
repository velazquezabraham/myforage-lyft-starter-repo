"""
Filename: carfactory.py
Date: 05/02/2023
Programmer: Abraham Velazquez
Describtion:
        CarFactory will be used in the Factory Method Design. This file will contain the
        CarFactory class that will be used to:
            - Changing the parts a car is composed of can be accomplished by modifying the
                corresponding create method in CarFactory.
            - Cars are created by calling the corresponding create method on CarFactory.
        NOTE: Consult the Factory Design pattern for additional contexct.
"""
#to create a car, we need the engine classes
from engine.capuletengine import CapuletEngine
from engine.sternmanengine import SternmanEngine
from engine.willoughbyengine import WilloughbyEngine

#to create a car, we need the battery classes
from battery.nubbinbattery import NubbinBattery
from battery.spindlerbattery import SpindleBattery

#to create a car we need to know about the car class, but do not inherit
from car import Car

#static methods class level, can only be called by the CarFactory class
class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        #The calliope car model needs an engine and a battery
        #create a calliope engine and a battery for this car model
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpindleBattery(last_service_date,current_date)
        car = car(engine,battery)
        return car 
     

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpindleBattery(last_service_date,current_date)
        car = car(engine,battery)
        return car 
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(last_service_date,current_date)
        car = car(engine,battery)
        return car 
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = car(engine,battery)
        return car 
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = car(engine,battery)
        return car 