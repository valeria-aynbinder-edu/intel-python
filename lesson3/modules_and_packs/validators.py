def get_int() -> int:
    while True:
        num = input("Insert a num: ")
        if num.isdigit():
            return int(num)


def get_date() -> tuple:
    pass


def get_time() -> tuple:
    print("Inside get_time of validators")


# print("end of validators")
