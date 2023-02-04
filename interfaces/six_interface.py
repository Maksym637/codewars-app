import abc


class SixKataInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def mean(self, town: str, s: str) -> float:
        raise NotImplementedError
    
    @abc.abstractmethod
    def variance(self, town: str, s: str) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def stock_list(self, list_of_art: list, list_of_cat: list) -> str:
        raise NotImplementedError
