# colors = {'red', 'white', 'black', 'blue'}
# print(colors)
# print(type(colors))

# print(colors[1])
# colors = {'red', 'white', 'black', 'blue', 'white'}
# print(colors)
# colors.add('green')
# colors.add('black')
# print(colors)


# l = [1, 2, 3, 2, 5, 6, 2, 5]
# s = set(l)
# print(list(s))
# print(s)
# print(l)
# l = set(l)

# s = set()
# l = []
# l = list()


lecture_days = {'sun', 'tue', 'wed'}
sport_days = {'mon', 'wed'}
sport_lecture_days = lecture_days.intersection(sport_days)
print(sport_lecture_days)
busy_days = lecture_days.union(sport_days)
print(busy_days)
week_days = {'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'}
avail_days = week_days.difference(busy_days)
print(avail_days)
print(avail_days - busy_days)


# s1 = frozenset({1, 2,3 ,4})















