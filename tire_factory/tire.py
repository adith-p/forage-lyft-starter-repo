from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, tire_arr):
        self.tire_arr = tire_arr

    @abstractmethod
    def tire_needs_services(self):
        pass
