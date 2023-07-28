from Battery import Battery
from datetime import datetime


class Nubbin_battery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def battery_needs_service(self):
        self.service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date+4)
        if self.service_threshold_date < datetime.today:
            return False
        return True
