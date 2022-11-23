# Write a program that receives 10 strings from a user,
# and prints the amount of strings with even length.

count = 0
even_cnt = 0
while count < 10:
    user_str = input("Insert a string: ")
    if len(user_str) % 2 == 0:
        even_cnt += 1
    count +=1
print(f"Total amount of strings with even len: {even_cnt}")