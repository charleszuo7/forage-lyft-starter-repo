from car import car 
from Batteries.Nubbin import NubbinBattery
from Engines.willoughby import WilloughbyEngine

class Rorschach(car):
    def __init__(self , last_service_date , current_mileage , last_service_milage):
        self.car_engine = WilloughbyEngine(current_mileage , last_service_milage)
        self.car_battery = NubbinBattery(last_service_date)
    
    def needs_service(self):
        if self.car_engine.needs_service() or self.car_battery.needs_service():
            return True
        else:
            return False
            # if neither one of engine and battery needs service, then the car doesnt need service
            

