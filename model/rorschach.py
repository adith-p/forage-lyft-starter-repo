from car import Car

from engine.willoughby_engine import WilloughbyEngine
from batteries.numbin_battery import Nubbin_battery
from tire_factory.carrigan import Carrigan


class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_arr):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = Nubbin_battery(last_service_date)
        self.tire = Carrigan(tire_arr)

        super().__init__(self.emgine, self.battery, self.tire)

    def need_service(self):
        return super().need_service()
