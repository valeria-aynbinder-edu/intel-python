# s = "hello"
# result = print(s)
# lower_str = s.lower()

# year = int(input("Insert a year: "))
# is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# a = "hello"
# year: int = 2000

def leap_year(year: int) -> bool:
    # global a
    # a = "bye"
    # print(a)
    print("inside leap_year")
    is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    return is_leap


def add_prefix(name: str):
    return ('Dr. ' + name).title()

# print(add_prefix('moshe'))

# 1, 3, 5, 7, 8, 10, 12
def is_31_days_month(month:int) -> bool:
    return month in [1, 3, 5, 7, 8, 10, 12]




# print(leap_year(1987))
# print(a)

# print(leap_year(2000))
# print(leap_year(1999))
# print(leap_year(2022))