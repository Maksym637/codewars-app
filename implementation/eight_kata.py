from interfaces.eight_interface import EightKataInterface
import math


class EightKata(EightKataInterface):

    def liters(self, time: float) -> int:
        return math.floor(time * 0.5)
    
    def get_volume_of_cuboid(self, length: float, width: float, height: float) -> float:
        return length * width * height
    
    def converter(self, mpg: float) -> float:
        return round((mpg * 1.609344) /  4.54609188, 2)
    
    def square_or_square_root(self, arr: list) -> list:
        result_arr = []
        for i in range(len(arr)):
            if(int(math.sqrt(arr[i])) ** 2 == arr[i]):
                result_arr.append(math.sqrt(arr[i]))
            else:
                result_arr.append(arr[i] ** 2)
        return result_arr
    
    def count_positives_sum_negatives(self, arr: list) -> list:
        if(len(arr) == 0):
            return []
        positive_numbers = len([x for x in arr if x > 0])
        negative_numbers = sum(x for x in arr if x < 0)
        return [positive_numbers, negative_numbers]
    
    def string_to_number(self, s: int) -> str:
        return int(s)
    
    def two_decimal_places(self, n: float) -> float:
        return round(n,2)
    
    def divisible_by(self, numbers: list, divisor: int) -> list:
        return [x for x in numbers if x % divisor == 0]
    