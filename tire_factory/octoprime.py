from tire import Tire


class Octaprime(Tire):
    def __init__(self, tire_arr):
        self.tire_arr = tire_arr

        super().__init__(tire_arr)

    def tire_needs_services(self):
        sum = 0
        for i in self.tire_arr:
            sum += i
        return sum <= 3
