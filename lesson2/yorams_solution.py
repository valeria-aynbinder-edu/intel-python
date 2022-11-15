# ex A
#====================
# i=1
# while i<11:
#     print(i)
#     i+=1

#ex C
#======================
# sum=0
# avg=0
# count = 0
#
# while True:
#     num=input("enter a number or $ to finish:")
#     if num == "$":
#         break
#     num=int(num)
#     count+=1
#     sum += num
#     # if num%10==0:
#     #     continue
#     #print ("your number is",num)
# avg=sum/count
#
# print (f"the sum is {sum} and the average is {avg}")


#ex E
#=========================
# strings_count=0
# char_count=0
# digit_count = 0
#
# while True:
#     str=input("enter a string or $ to finish:")
#     if str == "$":
#         break
#     strings_count+=1
#     char_count+=len(str)
#     if str.isdigit():
#         digit_count+=len(str)
#
#
# print (f"the number of strings is {strings_count}. the toatl characters is {char_count} and of it {digit_count} are digits")

#ex H
#=================
counter = 1
num = int(input("enter a number"))
while num//10>0:
    counter += 1
    num = num//10
print(f"the number contains {counter} digits")