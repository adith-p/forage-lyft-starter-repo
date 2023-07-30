
from car import Car

from engine.willoughby_engine import WilloughbyEngine
from batteries.spinder_battery import Spinder_battery
from tire_factory.octoprime import Octaprime


class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_arr):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = Spinder_battery(last_service_date)
        self.tire = Octaprime(tire_arr)

        super().__init__(self.engine, self.battery, self.tire)

    def needs_service(self):
        return super().need_service()
