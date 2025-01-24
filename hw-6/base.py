from abc import ABC
from exceptions_dir import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=10, started=False, fuel=0, fuel_consumption=1):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel != 0:
                self.started = True
                print("The vehicle has started")
            else:
                raise LowFuelError("The vehicle is not started")

    def move(self, fuel_consumption = 10):
        if self.started == True:
            if self.fuel != 0:
                self.fuel -= self.fuel_consumption
                print("The vehicle has moved")
            else:
                raise NotEnoughFuel("The vehicle is not started")
