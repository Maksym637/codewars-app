from implementation.seven_kata import SevenKata
from tests.test_data.data_seven_kata import data_task_1, data_task_1_error, data_task_2
import pytest


seven = SevenKata()


@pytest.mark.parametrize("arr,newavg,expected_result", data_task_1)
def test_task_1(arr, newavg, expected_result):
    assert seven.new_avg(arr, newavg) == expected_result

@pytest.mark.parametrize("arr,newavg", data_task_1_error)
def test_task_1_error(arr, newavg):
    with pytest.raises(ValueError):
        seven.new_avg(arr, newavg)

@pytest.mark.parametrize("n,expected_result", data_task_2)
def test_task_2(n, expected_result):
    assert seven.series_sum(n) == expected_result
