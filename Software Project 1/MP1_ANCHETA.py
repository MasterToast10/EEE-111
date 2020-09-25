# Rick's Great Plan for Success
#  1) Validate date range
#     [/] Within date limit
#     [ ] All inputs are integers
#     [ ] Valid dates
#  2) Number crunch
#     [ ] Compute total days
#     [ ] Compute weekdays
#     [ ] Compute leap years
#     [ ] Compute holidays falling on weekdays
#         [ ] New Year
#         [ ] Labor Day
#         [ ] All Saint's Day
#         [ ] Christmas
#  [ ] Compute work days

import datetime
from collections import namedtuple


DateRange = namedtuple("DateRange", ["start", "end"])


def get_user_input():
    """Gets date range as user input

    Raises:
        Exception: If input dates are out of date limit (January 1, 1971 to December 31, 2020)
        ValueError: If at least one of the following occurs:
            - At least one of the inputs is not an integer
            - At least one of the input dates is not a valid date

    Returns:
        DateRange: The start and end dates as datetime objects
    """
    start_date = tuple(map(int, [input("Enter start month: "), input(
        "Enter start day: "), input("Enter start year: ")]))
    end_date = tuple(map(int, [input("Enter end month: "), input(
        "Enter end day: "), input("Enter end year: ")]))

    if start_date[2] < 1971 or end_date[2] > 2020:
        raise Exception("Input dates outside date limit.")

    return DateRange(datetime.date(start_date[2], start_date[0], start_date[1]), datetime.date(end_date[2], end_date[0], end_date[1]))


try:
    dr = get_user_input()
    print(
        f"Start:\n\tMonth: {dr.start.month}\n\tDay: {dr.start.day}\n\tYear: {dr.start.year}")
    print(
        f"End:\n\tMonth: {dr.end.month}\n\tDay: {dr.end.day}\n\tYear: {dr.end.year}")
except:
    print("\nInvalid input. Exiting Program.")
    exit(1)
