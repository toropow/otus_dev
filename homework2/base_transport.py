from abc import ABCMeta, abstractmethod


class Transport(metaclass=ABCMeta):
    color: str = None
    weight: int = None
    fuel_consumption_100km: int = None

    @abstractmethod
    def make_sound(self) -> str:
        raise NotImplemented

    @abstractmethod
    def way(self) -> str:
        raise NotImplemented
