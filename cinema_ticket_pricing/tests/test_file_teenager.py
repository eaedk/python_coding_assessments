# importation of the solution function to test
from cinema_ticket_pricing.file import solution


# Teenager tests
def test_solution_day_weekday_teenager():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=1, is_day=True, is_Wednesday=True, is_weekend=False)
    expected_output = 100

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_night_weekday_teenager():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=1, is_day=False, is_Wednesday=False, is_weekend=False)
    expected_output = 270

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_day_weekend_teenager():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=1, is_day=True, is_Wednesday=False, is_weekend=True)
    expected_output = 55.25

    output = solution(**valid_inputs)

    assert output == expected_output


def test_solution_night_weekend_teenager():
    """This is the test for price in some conditions"""
    valid_inputs = dict(age_class=1, is_day=False, is_Wednesday=False, is_weekend=True)
    expected_output = 228

    output = solution(**valid_inputs)

    assert output == expected_output
