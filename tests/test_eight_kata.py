from implementation.eight_kata import EightKata
from tests.test_data.data_eight_kata import (
    data_task_1, data_task_2, data_task_3, data_task_4, 
    data_task_5, data_task_6, data_task_7, data_task_8
    )
import pytest


eight_kata = EightKata()


@pytest.mark.parametrize("time,expected_result", data_task_1)
def test_task_1(time, expected_result):
    assert eight_kata.liters(time) == expected_result

@pytest.mark.parametrize("length,width,height,expected_result", data_task_2)
def test_task_2(length, width, height, expected_result):
    assert eight_kata.get_volume_of_cuboid(length, width, height) == expected_result

@pytest.mark.parametrize("mpg,expected_result", data_task_3)
def test_task_3(mpg, expected_result):
    assert eight_kata.converter(mpg) == expected_result

@pytest.mark.parametrize("arr,expected_result", data_task_4)
def test_task_4(arr, expected_result):
    assert eight_kata.square_or_square_root(arr) == expected_result

@pytest.mark.parametrize("arr,expected_result", data_task_5)
def test_task_5(arr, expected_result):
    assert eight_kata.count_positives_sum_negatives(arr) == expected_result

@pytest.mark.parametrize("s,expected_result", data_task_6)
def test_task_6(s, expected_result):
    assert eight_kata.string_to_number(s) == expected_result

@pytest.mark.parametrize("n,expected_result", data_task_7)
def test_task_7(n, expected_result):
    assert eight_kata.two_decimal_places(n) == expected_result

@pytest.mark.parametrize("numbers,divisor,expected_result", data_task_8)
def test_task_8(numbers, divisor, expected_result):
    assert eight_kata.divisible_by(numbers, divisor) == expected_result
