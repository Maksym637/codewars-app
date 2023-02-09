from implementation.six_kata import SixKata
from tests.test_data.data_six_kata import data_task_1, data_task_2
import pytest


six_kata = SixKata()


@pytest.mark.parametrize("town,s,expected_mean,expected_variance", data_task_1)
def test_task_1(town, s, expected_mean, expected_variance):
    assert (six_kata.mean(town, s), six_kata.variance(town, s)) == (expected_mean, expected_variance)

@pytest.mark.parametrize("list_of_art,list_of_cat,expected_result", data_task_2)
def test_task_2(list_of_art, list_of_cat, expected_result):
    assert six_kata.stock_list(list_of_art, list_of_cat) == expected_result
