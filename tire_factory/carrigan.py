from tire import Tire


class Carrigan(Tire):
    def __init__(self, tire_arr):
        self.tire_arr = tire_arr

        super().__init__(tire_arr)

    def tire_needs_services(self):
        for i in self.tire_arr:
            return i >= 0.9
