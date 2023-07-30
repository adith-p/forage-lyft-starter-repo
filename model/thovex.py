
from car import Car

from engine.capulet_engine import CapuletEngine
from batteries.numbin_battery import Nubbin_battery
from tire_factory.carrigan import Carrigan


class Thovex(Car):

    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_arr):

        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = Nubbin_battery(last_service_date)
        self.tire = Carrigan(tire_arr)

        super().__init__(self.engine, self.battery)

    def needs_service(self):
        super().need_service()
