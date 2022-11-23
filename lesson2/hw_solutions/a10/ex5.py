# Write a program that receives strings from a user until the user
# inserts a special character $ that indicates the end of the input.
# After $ has been inserted, the program should print out the
# total number of strings inserted by the user,
# total number of all the characters inserted by the user,
# and total number of digits inserted by the user (in strings that contain digits only).

str_count = 0
total_chars = 0
total_digits = 0
while True:
    user_str = input("Insert a string: ")
    if user_str == '$':
        break
    else:
        str_count += 1
        total_chars += len(user_str)
        if user_str.isdigit():
            total_digits += len(user_str)

print(f"Total strings received: {str_count}")
print(f"Total chars received: {total_chars}")
print(f"Total digits received: {total_digits}")

