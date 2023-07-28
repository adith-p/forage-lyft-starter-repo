
from batteries.spinder_battery import Spinder_battery
from engine.sternman_engine import SternmanEngine
from car import Car


class Palindrome(Car):
    def __init__(self, last_service_date, warning_indicator_on):
        self.engine = SternmanEngine(warning_indicator_on)
        self.battery = Spinder_battery(last_service_date)

        super().__init__(self.engine, self.battery)

    def need_service(self):
        return super().need_service()
