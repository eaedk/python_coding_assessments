# importation of the solution function to test
from pandas_data_cleaning.file import solution
import pandas as pd


def test_solution_valid_inputs():
    """This is the test for the implemented solution passing
    valid inputs"""
    valid_inputs = ["pandas_data_cleaning/data/titanic.csv"]
    expected_outputs = [pd.read_csv("pandas_data_cleaning/tests/titanic_clean.csv")]
    outputs = []

    for input in valid_inputs:
        outputs.append(solution(input).reset_index(drop=True).sort_values(by=["Name"]))

    assert expected_outputs == expected_outputs
