def leap_year(year: int) -> bool:
    is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    return is_leap


def is_31_days_month(month: int) -> bool:
    return month in [1, 3, 5, 7, 8, 10, 12]


def get_days_in_month(month: int, year: int) -> int:
    if is_31_days_month(month):
        return 31
    elif month == 2:
        # return 29 if leap_year(year) else 28
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30


print("Hello and Welcome")
command = input("What would you like to do? 'y' for detecting leap year, 'm' for days in month")
if command == 'y':
    year = int(input("Insert year: "))
    if leap_year(year):
        print(f"leap year")
    else:
        print("not leap year")
elif command == 'm':
    year = int(input("Insert year: "))
    month = int(input("Insert month: "))
    days = get_days_in_month(month, year)
    print("There are ", days," days in month")