from homework2.base_transport import Transport
from homework2.data_classes import Capitan


class Boat(Transport):
    color = 'White'
    weight = 1000
    fuel_consumption_100km = 100
    type_engine = 'diesel'

    def make_sound(self) -> str:
        return 'Tooootoooo'

    def way(self) -> str:
        return 'only by water'

    def create_signal_sos(self, signal) -> str:
        return f"Warning {signal}"


class Yacht(Boat):
    def __init__(self, name, age, experience, salary, ability_swim, radio):
        self.manager = Capitan(name=name, age=age, experience=experience, salary=salary, ability_swim=ability_swim)
        if radio is False:
            raise Exception('The boat must have a radio')

    def cruise(self):
        pass

    def __repr__(self):
        return f'''
                This is {self.__class__.__name__}
                Color: {Yacht.color}
                Weight: {Yacht.weight}
                Consumption per 100 km: {Yacht.fuel_consumption_100km}
                Type of engine: {Yacht.type_engine}
                Capitan name: {self.manager.name}
                Capitan age:  {self.manager.age} 
                Capitan experience {self.manager.experience},
                Capitan star career at: {self.manager.career_start_age()}
'''