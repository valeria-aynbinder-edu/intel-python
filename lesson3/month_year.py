def leap_year(year: int) -> bool:
    is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    return is_leap


def is_31_days_month(month: int) -> bool:
    return month in [1, 3, 5, 7, 8, 10, 12]


def get_days_in_month(month: int, year: int) -> int: