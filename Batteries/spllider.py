from Batteries.battery import battery
from datetime import datetime
class SpindlerBattery(battery):
    def __init__(self, date):
        super().__init__(date)
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date:
            return False
        else:
            return True
