from car import car 
from Batteries.spllider import SpindlerBattery
from Engines.sternman import SternmanEngine

class Palindrome(car):
    def __init__(self , last_service_date , warninglighton):
        self.car_engine = SternmanEngine(warninglighton)
        self.car_battery = SpindlerBattery(last_service_date)

    def needs_service(self):
        if self.car_engine.needs_service() or self.car_battery.needs_service():
            return True
        else:
            return False
            # if neither one of engine and battery needs service, then the car doesnt need service
            

