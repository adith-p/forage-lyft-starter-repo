from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, currt_mileage, last_service_mileage, warning_indicator_on=False):
        self.currt_mileage = currt_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_indicator_on = warning_indicator_on

    @abstractmethod
    def engine_should_be_serviced(self):
        pass
