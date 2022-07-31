from Batteries.Nubbin import NubbinBattery
from datetime import datetime

date = datetime.today().date().replace(year = datetime.today().date().year - 4)
bat = NubbinBattery(date)
print(bat.needs_service())