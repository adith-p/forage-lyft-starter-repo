from batteries.Battery import Battery
from Engine import Engine


class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def engine_should_be_serviced(self):
        return self.engine.engine_should_be_serviced()

    def battery_needs_service(self):
        return self.battery.battery_needs_service()

    def need_service(self):
        return self.engine_should_be_serviced() or self.battery_needs_service()
