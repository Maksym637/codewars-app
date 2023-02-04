import abc


class SevenKataInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def new_avg(self, arr: list, newavg: float) -> float:
        raise NotImplementedError
    
    @abc.abstractmethod
    def series_sum(self, n: int) -> str:
        raise NotImplementedError
