# print("Hello World")
# name = input("Insert your name: ")
# print(name)
#
# # Print the id of the address in the memory
# print(id(name))

# math operators
# print("5+7")
# print(5+7)
# print("5+7 =", 5+7)
# print("5*7 =", 5*7)
# print("5/7 =", 5/7)
# print("5-7 =", 5-7)

# python documentation
# https://docs.python.org/3/tutorial/introduction.html#numbers
# modulus
# print("5 % 2 =", 5 % 2)
# print("19 % 4 =", 19 % 4)
#
# # floor division
# print("5 // 2 =", 5 // 2)
# print("19 // 4 =", 19 // 4)
#
# # power
# print('3 ** 4 =', 3 ** 4)


# name = input("Insert your name: ")

# option 1
# year = int(input("Insert your birth year: "))

# option 2
# year = input("Insert your birth year: ")
# year = int(year)

# print("The type of year is: ", type(year))
# age = 2022 - year
# print(name, "is", age, "years old")


# Variable types

name = "Hello"  # string
num = 5  # int
float_num = 2.5  # float

# Exercise
# Get movie length in seconds
# and display the length in the format hh:mm:ss

# total_seconds = int(input("Insert movie length in seconds: "))
# total_minutes = total_seconds // 60
# seconds = total_seconds % 60
# hours = total_minutes // 60
# minutes = total_minutes % 60
#
# # print("The length of the movie is:", hours, ":", minutes, ":", seconds)
# print(f"The length of the movie is: {hours}:{minutes}:{seconds}")

# String formatting
# print(f"5+6={5+6}")  # 5+6=11
# print("5+6={5+6}")

# String
# text1 = "Hello world"
# text2 = 'Hello world'
# sentence1 = 'She said: "My name is Valeria"'
# sentence2 = "She said: 'My name is Valeria'"
# sentence3 = "She said: \"My name is Valeria\""
# # print("Hello world\nBye")
# # long_text = "Hello\nI'm Valeria\nBye"
# long_text = """Hello
# I'm Valeria
# Bye
# """
# long_text = '''Hello
# I'm Valeria
# Bye
# '''
# long_text = f'''Hello
# I'm {name}
# Bye
# '''
# print(long_text)


# Bool type, comparison operators, logical operators
# print(6 < 7)
# print(6 > 7)
# print(type(6 > 7))
# my_bool = True
# my_other_bool = False
# > < >= <=
# 5 == 8
# 5 != 8

# age = int(input("Your age: "))
# retired = age >= 65
# print(f"Is retired: {retired}")

# print(True and True)

# True and True => True
# True and False => False
# False and True => False
# False and False => False

# print(True or False)
# True or True => True
# True or False => True
# False or True => True
# False or False => False


# beer <= 0.3
# wine <= 0.2
# drink_type = input("Drink type (beer/wine): ")
# qty = float(input("Insert quantity: "))
# can_drive = (drink_type == 'beer' and qty <= 0.3) or \
#             (drink_type == 'wine' and qty <= 0.2)
# print(f"Can drive: {can_drive}")

# if-else-elif
# drink_type = input("Drink type (beer/wine/water/whiskey): ")
# if drink_type == "beer" or drink_type == "wine":
#     qty = float(input("Insert quantity: "))
#     can_drive = (drink_type == 'beer' and qty <= 0.3) or \
#                 (drink_type == 'wine' and qty <= 0.2)
#     print(f"Can drive: {can_drive}")
# elif drink_type == 'water':
#     print("You can drive")
# elif drink_type == 'whiskey':
#     print("You can not drive")
# else:
#     print("Invalid input")
#
# print("Bye")
#
#
# if drink_type == 'water':
#     print("water")

# match case

# drink_type = input("Drink type (beer/wine/water/whiskey): ")
# match drink_type:
#     case "water":
#         print("You can drive")
#     case "whiskey":
#         print("You cannot drive")
#     case "beer" | "wine":
#         qty = float(input("Insert quantity: "))
#         can_drive = (drink_type == 'beer' and qty <= 0.3) or \
#                     (drink_type == 'wine' and qty <= 0.2)
#         print(f"Can drive: {can_drive}")
#     case _:
#         print("Invalid input")


# is_leap_year
# Write a code that receives the year as input and prints whether
# the year is a leap year or not. To be a leap year,
# the year number must be divisible by four –
# except for end-of-century years, which must be divisible by 400.
# This means that the year 2000 was a leap year, although 1900 was not.
# 2020, 2024 and 2028 are all leap years.
# 1990, 1994, 1998, ... - leap

# year = int(input("insert year: "))
# is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


# year = int(input("Insert year : "))
# flag = (year % 400) + (year % 100)
# if flag == 0:
#     print("Year is not a Leap year")
# else:
#     flag = year % 4
#     if flag> 0:
#         print("Year is not a Leap year")
#     else:
#         print("Year is Leap year")
# print ("Bye")


# temp
# sun / rain / snow
# temp < 0 => coat
# temp 0 < temp < 20 => sweater
# temp >= 20 => t-shirt
# rain => umbrella
# sun => sunglasses
# temp = int(input("Insert temperature: "))
# weather = input("Insert weather")  # sun / rain / snow / cloudy
# if temp < 0:
#     print("coat")
# elif 0 <= temp <= 20:
#     print("Sweater")
# else:
#     print("T-shirt")
#
# if weather == 'rain':
#     print("umbrella")
# elif weather == 'sun':
#     print("take sunglasses")
# optional
# else:
#     pass

# built-in functions
# https://docs.python.org/3/library/functions.html
# print / type / id
# num = int(input("Insert a num: "))
# print(abs(num))
# t = divmod(9, 5)
# print('divmod(9, 5)=', t)
# num = float(input("Insert a num: "))
# print(round(num))
# print(round(num, 3))


# List
names = ['Valeria', 'Elad', 'Maria', 'Moshe', 'David', 'Tamir']
# print(type(names))
# print(names)
# print(names[0])
# print(type(names[0]))
# print(names[2])
# print(names[-1])
# print(names[-3])
# print(names[1:4])
# print(names[-1:-4:-1])
# print(names[1:4:5])
# print(names[2:3:1])
# print(names[2])
# print(names[2:])
# print(names[:-1])
# print(names[::-1])
# print(names[-1::-1])

# grades = [87, 90, 56, 67]

# various = ['Moshe', 23874, True, 4.5, 345]
# various[2]  # bool
# various[0]  # str


# nested_list = [['Moshe', 90], ['Valeria', '87'], ['Tamir', '70']]
# nested_list[1][1]

# l = []
# l.append("Valeria")
# print(l)
# l.append("David")
# print(l)
# l.insert(0, 'David')
# l.append('Tamir')
# l.append('Elad')
# l.append('Valeria')
# print(l)  # ['David', 'Valeria', 'Tamir', 'Elad', 'Valeria']
# l.pop(2)
# print(l)
# l.remove('Valeria')
# print(l)
# print(len(l))
# l1 = []
# l1 = ['Valeria']
# print(l.index('Elad', 1, 2))
#
# grades = [80, 100, 56, 100, 90]
# print(grades.count(100))
#
# print(min(grades))
# print(max(45, 100, 345, 1, 23))

# text = "Hello World, the sun is shining and thw life is beautiful"
# print(text[-1])
# print(type(text[-1]))
# print(text[::-1])
# print(len(text))
# print(text.index("el"))
# print(text.index("o", 5))
# print(text.find("ttt"))
# print(text.split(" ")[-1])
# print(text.split(","))


# Implement a code that receives the layout of the seats in
# the aircraft as letters and returns the layout as numbers.
# For example:
# ABC DEF => 3 3
# AB CDEF GH => 2 4 2
# You can assume that the maximum number of seat “batches” in any aircraft is 3.
# plane = input('enter plane structure: ')
# spl = plane.split(' ')
#
# if len(spl) == 2:
#      print(f'plane structure is ', len(spl[0]), len(spl[1]))
# elif len(spl) == 3:
#     print(f'plane structure is ', len(spl[0]), len(spl[1]), len(spl[2]))


# str_list = ['asd', 'asdasfhs', 'sdfasdf', 'dfgdafg']
# print(' '.join([str(len(x)) for x in str_list]))




# String slicing
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1



# Implement a code that receives the aircraft seat number (4J, 34A, etc…)
# and aircraft layout like in the previous exercise (ABC DEF, ABC DEFGH IJK,...).
# Your code should print out 3 things:
# Row number
# Seat Character
# Print whether the user is going to sit near the window, in the aisle, or in the middle.
# For example, for the input: 4J and ABC DEFG HIJ: the output should be:
# Row number: 4
# Char: J
# Window
#
# You can assume that row number is a maximum 2-digit number,
# and seat Char is always a one single char.


seat = input("Insert seat number (for example, 13B): ")
structure = input("Insert aircraft structure (for example: ABC DEFG HIJ): ")

# 13B
# 4C

if seat[1].isdigit():
    row = seat[0:2]
else:
    row = seat[0]

# if len(seat) == 2:

seat_char = seat[-1]
print(f"Row: {row} | Seat char: {seat_char}")
# 13B
# 4C
# ABC DEF
seat_char_idx = structure.index(seat_char)
if seat_char_idx == len(structure)-1 or seat_char_idx == 0:
    print("window")
elif structure[seat_char_idx-1] != " " and structure[seat_char_idx+1] != " ":
    print("middle")
else:
    print("aisle")
