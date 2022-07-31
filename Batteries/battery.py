from datetime import datetime

class battery():
    def __init__(self , date):
        self.last_service_date = date
        self.current_date = datetime.today().date()
        pass

    def needs_service(self):
        pass
        