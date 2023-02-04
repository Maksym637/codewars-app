import abc


class EightKataInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def liters(self, time: float) -> int:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_volume_of_cuboid(self, length: float, width: float, height: float) -> float:
        raise NotImplementedError
    
    @abc.abstractmethod
    def converter(self, mpg: float) -> float:
        raise NotImplementedError
    
    @abc.abstractmethod
    def square_or_square_root(self, arr: list) -> list:
        raise NotImplementedError
    
    @abc.abstractmethod
    def count_positives_sum_negatives(self, arr: list) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def string_to_number(self, s: int) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def two_decimal_places(self, n: float) -> float:
        raise NotImplementedError
    
    @abc.abstractmethod
    def divisible_by(self, numbers: list, divisor: int) -> list:
        raise NotImplementedError
