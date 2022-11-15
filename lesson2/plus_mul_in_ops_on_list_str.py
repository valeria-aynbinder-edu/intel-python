# in
names = ['moshe', 'david', 'orly']
# print('valeria' in names)
# print('david' in names)
# ret_val = names.index('david')
# print(ret_val)
# ret_val = names.index('aaa')
# print(ret_val)
# 'moshe' not in names


text = "Hello, my name is Valeria and I like AI"
# print("," in text)
# print("!" in text)
# print("and" in text)
# print(text.index("and"))
# print(text.index("apple"))
# print(text.find("and"))
# print(text.find("apple"))

# countries and cities
# countries = ["Israel", "UK", "Ukraine", "US"]
# cities = [["Tel Aviv", "Haifa", "Yerucham", "Petah Tikva"],
#           ["London", "Manchester"],
#           ["Kyiv", "Cherson"],
#           ["New York", "Los Angeles", "Las Vegas"]]
# state=input("enter state")
# city=input("enter city")
#
# if state in countries:
#     index=countries.index(state)
#     if city in cities[index]:
#         print (f"the city {city} is in {state}")
#     else:
#         print (f"the city {city} is not in {state}")
# else:
#     print("The country is not in the list")


# + *
# print(6+7)
# print(6*7)
# print("apple" + "pear")
# word1 = "apple"
# word2 = "pear"
# word3 = word1 + word2
# word3 = "".join([word1, word2])
# word3 = f"{word1}{word2}"
# print(word1, word2, word3)
# word3 = word1 * word2
# word3 = word1 * 3
# print(word3)

fruits = ['mangustin', 'salak', 'passionfruit', 'dragonfruit']
vegs = ['tomato', 'cucumber', 'onion']
# new_list = fruits + vegs
# print(new_list)
# new_list = fruits * vegs
# new_list = fruits * 2

# new_list = fruits + vegs # a new list is created
# fruits.extend(vegs) # no new list! fruits is updated
# print(new_list)
# print(fruits)
# print(id(new_list), id(fruits))
# print(new_list is fruits)
# print(id(new_list) == id(fruits))

# print(result)

# python typing
# num = 5
# num: int = 5
# num = "tttt"
# print(num)

# countries: list = ["Israel", "UK", "Ukraine", "US"]
# cities: list = [["Tel Aviv", "Haifa", "Yerucham", "Petah Tikva"],
#           ["London", "Manchester"],
#           ["Kyiv", "Cherson"],
#           ["New York", "Los Angeles", "Las Vegas"]]
#
# state: str = input("enter state")
# city: str = input("enter city")
#
# if state in countries:
#     index: int = countries.index(state)
#     if city in cities[index]:
#         print(f"the city {city} is in {state}")
#     else:
#         print(f"the city {city} is not in {state}")
#     # index = input("dsfsdf")
# else:
#     print("The country is not in the list")