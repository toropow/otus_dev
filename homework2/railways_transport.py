from homework2.base_transport import Transport
from homework2.data_classes import TrainManager


class Train(Transport):
    color = 'Green'
    weight = 5000
    fuel_consumption_100km = 200
    tank_capacity = 10000

    @classmethod
    def make_sound(cls) -> str:
        return 'ChuhChuh... ToooTooo'

    def way(self) -> str:
        return 'Only by railways'

    def track_distance(self) -> int:
        return int(self.tank_capacity / self.fuel_consumption_100km)


class Locomotive(Train):
    weight = 2000
    fuel_consumption_100km = 300
    tank_capacity = 20000

    def __init__(self, name, age, experience, salary, personal_car, fuel_level):
        self.manager = TrainManager(name=name, age=age, experience=experience, salary=salary, personal_car=personal_car)
        self.fuel_level = fuel_level
        self.engine_check(self.fuel_level)

    def engine_check(self, fuel_level):
        if fuel_level <= 0:
            raise Exception('Fuel level must be greater than zero')

    def make_stop(self):
        return "Stooooop!"

    def __repr__(self):
        return f'''
                This is {self.__class__.__name__}
                Color: {Locomotive.color}
                Weight: {Locomotive.weight}
                Consumption per 100 km: {Locomotive.fuel_consumption_100km}
                Capacity of tank: {Locomotive.tank_capacity}
                Rain train sound: {Locomotive.make_sound()}
                Train manager name: {self.manager.name}
                Train manager age:  {self.manager.age} 
                Train manager experience {self.manager.experience},
                Train manager star career at: {self.manager.career_start_age()
        }
'''
