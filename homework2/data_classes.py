from dataclasses import dataclass


@dataclass
class Manager:
    name: str
    age: int
    experience: int
    salary: int

    def career_start_age(self):
        return self.age - self.experience

    def __post_init__(self):
        self.experience = int(self.experience)
        self.salary = int(self.salary)
        self.age = int(self.age)


@dataclass
class Capitan(Manager):
    ability_swim: bool = True


@dataclass
class TrainManager(Manager):
    personal_car: bool = True
