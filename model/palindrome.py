from car import Car

from batteries.spinder_battery import Spinder_battery
from engine.sternman_engine import SternmanEngine
from tire_factory.octoprime import Octaprime


class Palindrome(Car):
    def __init__(self, last_service_date, warning_indicator_on, tire_arr):
        self.engine = SternmanEngine(warning_indicator_on)
        self.battery = Spinder_battery(last_service_date)
        self.tire = Octaprime(tire_arr)

        super().__init__(self.engine, self.battery)

    def need_service(self):
        return super().need_service()
