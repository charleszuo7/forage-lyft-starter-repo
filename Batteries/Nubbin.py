from flask_login import FlaskLoginClient
from Batteries.battery import battery
from datetime import datetime
class NubbinBattery(battery):
    def __init__(self, date):
        super().__init__(date)
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date:
            return True
            #meaning need service, battery is out of date
        else:
            return False
            # meaning no repair, battery is good 
