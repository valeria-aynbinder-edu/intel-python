l = [['Paris', 'London', 'New York'],
     [45, True, 5.5, 'hello'],
     -3,
     [5, ['#', '$', '%', '^', [10, 20, 30, 40]]],
     [['a'], ['b'], 'c', [['d']]]]


# -3 (int)
print(l[2])

# 5.5 (float)
print(l[1][2])

# ['New York', 'London', 'Paris']
print(l[0][::-1])

# [[45, True, 5.5, 'hello'], -3]
print(l[1:3])

# '^'(str)
print(l[-2][-1][-2])

# 'a' (str)
print(l[-1][0][0])

# ['b'](str)
print(l[-1][1])


# 'd' (str)
print(l[-1][-1][-1][-1])

# [20, 40](list)
print(l[-2][-1][-1][1::2])

# ['^', '#'] (list)
print(l[-2][-1][-2::-3])