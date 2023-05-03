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

#to define abstract methods inside the CarFactory class
from abc import ABC, abstractmethod
#to know about the car, but do not inherit
from car import Car
"""
    This functions will return a car object.

    current_date        [date]
    last_service_date   [date]
    current_mileage     [int]
    last_service_mileage[int]

    returns a car object
"""

#define the abstract CarFactory class
class CarFactory(ABC):
    @abstractmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass

    @abstractmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass
    
    @abstractmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        pass

    @abstractmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass

    @abstractmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass

