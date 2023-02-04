from interfaces.seven_interface import SevenKataInterface
import math


class SevenKata(SevenKataInterface):

    def new_avg(self, arr: list, newavg: float) -> float:
        sum_arr = sum(arr)
        size = len(arr) + 1
        result = math.ceil(newavg * size - sum_arr)
        if(result <= 0):
            raise ValueError
        return result
    
    def series_sum(self, n: int) -> str:
        if(n == 0): return "0.00"
        cnt, init, result = 1, 4, 1
        while(cnt < n):
            result += 1 / init
            init += 3
            cnt += 1
        return "{:.2f}".format(result)
