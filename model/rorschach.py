

from engine.willoughby_engine import WilloughbyEngine
from batteries.numbin_battery import Nubbin_battery
from car import Car


class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = Nubbin_battery(last_service_date)

        super().__init__(self.emgine, self.battery)

    def need_service(self):
        return super().need_service()
