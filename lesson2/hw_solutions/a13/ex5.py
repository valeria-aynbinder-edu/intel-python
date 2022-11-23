# Get 10 dates from the user.
# The date is in the following format: dd.mm.yyyy (no need to check).
# After you get all the 10 dates,
# print the amount of dates in winter, autumn, sprint, summer, and print the dates themselves.
# The output should look something like:
#
# You entered 2 dates in winter:
# 11.12.2013
# 05.01.1999
#
# You entered 8 dates in summer:
# 16.08.2012
# 05.07.1999
#
#     ...

dates_num = 5
seasons = ['winter', 'summer', 'autumn', 'spring']
dates_per_season = [[], [], [], []]

for i in range(dates_num):
    date = input("Insert date: ")
    date_split = date.split(".")
    month = int(date_split[1])
    if month in [12, 1, 2]:
        dates_per_season[0].append(date)
    elif month in [3,4,5]:
        dates_per_season[3].append(date)
    elif month in [6,7,8]:
        dates_per_season[1].append(date)
    else:
        dates_per_season[2].append(date)

for i, season in enumerate(seasons):
    print(f"You inserted {len(dates_per_season[i])} dates in {season}:")
    print(dates_per_season[i])