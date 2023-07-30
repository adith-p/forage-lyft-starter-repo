from Battery import Battery
from Engine import Engine
from tire_factory import tire


class Car(Engine, Battery, tire):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def engine_should_be_serviced(self):
        return self.engine.engine_should_be_serviced()

    def battery_needs_service(self):
        return self.battery.battery_needs_service()

    def tire_needs_services(self):
        return self.tire.tire_needs_services()

    def need_service(self):
        return self.engine_should_be_serviced() or self.battery_needs_service() or self.tire_needs_services()
