# int, float, str, bool, list,
# tuple

# my_tuple = (10, 20, 30, 40)
# my_tuple = 10, 20, 30, 40
# print(my_tuple)
#
# my_list = [1,2,3,4,5]
# my_list[0] = 40
# print(my_list)

# my_tuple[0] = 40
# my_tuple.

# print(my_tuple[3])


# 11.02.1987
# def get_date() -> (int, int, int):
#     full_date = input("Insert a date: ")
#     split_list = full_date.split(".")
#     return int(split_list[0]), int(split_list[1]), int(split_list[2])
#
#
# # ret_val = get_date()
# # print(ret_val)
# d, m, y = get_date()
# print(d, m, y)

# def get_date() -> (int, int, int):
#     full_date = input("Insert a date: ")
#     day, month, year = full_date.split(".")
#     return int(day), int(month), int(year)
#
# d, m, y = get_date()
# print(y)


# int('5')
# float('5.6')
# print(list('hello'))
# print(tuple('hello'))
# print(tuple([10, 11, 12, "gfgf"]))
#
#
# (12, 3, 4, 12, 7, 3, 8)
# (12, 3, 4, 7, 8)


def get_unique(t: tuple) -> tuple:
    unique_elems = []
    for elem in t:
        if elem not in unique_elems:
            unique_elems.append(elem)
    return tuple(unique_elems)

print(get_unique((12, "h", "ttt", 12, 3, "ttt", 12)))