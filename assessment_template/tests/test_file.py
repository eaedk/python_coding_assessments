# importation of the solution function to test
from assessment_template.file import solution


def test_solution_valid_inputs():
    """This is the test for the implemented solution passing
    valid inputs"""
    valid_inputs, expected_outputs = [], []
    outputs = []

    for input in valid_inputs:
        outputs.append(solution(input))

    assert outputs == expected_outputs


def test_solution_non_valid_inputs():
    """This is the test for the implemented solution passing
    non valid inputs"""
    non_valid_inputs, expected_outputs = [], []
    outputs = []

    for input in non_valid_inputs:
        outputs.append(solution(input))

    assert outputs == expected_outputs
