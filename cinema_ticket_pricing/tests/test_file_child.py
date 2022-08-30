# importation of the solution function to test
from cinema_ticket_pricing.file import solution

# Child tests
def test_solution_day_Wednesday_child():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=0, is_day=True, is_Wednesday=True, is_weekend=False)
    expected_output = 60

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_night_Wednesday_child():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=0, is_day=False, is_Wednesday=True, is_weekend=False)
    expected_output = 270

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_day_otherWeekday_child():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=0, is_day=True, is_Wednesday=False, is_weekend=False)
    expected_output = 90

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_day_weekend_child():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=0, is_day=True, is_Wednesday=False, is_weekend=True)
    expected_output = 76.5

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_night_weekend_child():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=0, is_day=False, is_Wednesday=False, is_weekend=True)
    expected_output = 240

    output = solution(**valid_inputs)

    assert output == expected_output
