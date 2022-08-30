# importation of the solution function to test
from cinema_ticket_pricing.file import solution


# Adult tests
def test_solution_day_weekday_adult():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=2, is_day=True, is_Wednesday=False, is_weekend=False)
    expected_output = 100

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_night_weekday_adult():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=2, is_day=False, is_Wednesday=False, is_weekend=False)
    expected_output = 260

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_day_weekend_adult():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=2, is_day=True, is_Wednesday=False, is_weekend=True)
    expected_output = 85

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_night_weekend_adult():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=2, is_day=False, is_Wednesday=False, is_weekend=True)
    expected_output = 240

    output = solution(**valid_inputs)

    assert output == expected_output
