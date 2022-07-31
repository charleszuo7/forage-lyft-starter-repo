from Engines.engine import engine

class CapuletEngine(engine):
    def __init__(self , cur_mile , last_service_mile):
        super().__init__()
        self.current_mileage = cur_mile
        self.last_service_mileage = last_service_mile
        
    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True 
        else:
            return False