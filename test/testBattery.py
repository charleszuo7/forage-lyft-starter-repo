import unittest
from datetime import date

from Batteries.Nubbin import NubbinBattery
from Batteries.spllider import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2011-03-25")
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2017-11-10")
        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2011-03-25")
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2017-11-10")
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())