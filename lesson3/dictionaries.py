d1 = {
    11111111: 'Valeria Aynbinder',
    22222222: 'Israel Israeli',
    33333333: 'Ron Cohen'
}
# print(d1)

# print(d1[22222222])

weather = {
    'paris': 10,
    'london': 12.5,
    'tel aviv': 20,
    'new york': 0.5
}

# print(weather['london'])


grades = {
    111: [90, 67, 80],
    222: [],
    333: [97, 60]
}
# print(grades)
# grades[444] = [67, 80]
# print(grades)
# grades[222] = [78, 87, 90]
# print(grades)
# grades[333].append(79)
# print(grades)
# grades[111][0] = 92
# print(grades)
# # del grades[111]
# # grades.pop(111)
# print(grades)

#
# print(grades[333])

stock_price = {
    ('TSLA', '10.11.2022'): 300,
    ('AAPL', '10.11.2022'): 230,
    ('TSLA', '1.11.2022'): 300,
    ('AAPL', '5.11.2022'): 300,
}

# print(stock_price[('AAPL', '5.11.2022')])

person = {
    'id': 333333333,
    'first_name': "Valeria",
    'last_name': 'Aynbinder',
    'address': 'Netanya',
    'phone': '054-9999999',
    'birth_year': 1987
}

# print(person['birth_year'])


people = {
    333333333: {
        'id': 333333333,
        'first_name': "Valeria",
        'last_name': 'Aynbinder',
        'address': 'Netanya',
        'phone': '054-9999999',
        'birth_year': 1987
    },
    444444444: {
        'id': 444444444,
        'first_name': "Ron",
        'last_name': 'Cohen',
        'address': 'Haifa',
        'phone': '054-66666666',
        'birth_year': 1990
    },
}

# print(people[444444444]['address'])

# for person_id in people:
#     print(people[person_id]['phone'])

# a, b = 3, 4

for person_id, person in people.items():
    print(person['phone'])


# for elem in people.items():
#     print(elem)

