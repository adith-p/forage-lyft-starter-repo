from car import Car
from engine.capulet_engine import CapuletEngine
from batteries.spinder_battery import Spinder_battery


class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = Spinder_battery(last_service_date)

        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().need_service()
