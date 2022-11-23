# Write a program that receives student names and their grades one by one.
# The program should continue running until the user inserts "$$$"
# to indicate end of input. After receiving "$$$",
# the program should print all the names of the students and
# amount of the names received.
# In addition the program should print an average grade.

names = []
grades = []
while True:
    name = input("Insert a name or $$$ to finish: ")
    if name == '$$$':
        break
    names.append(name)
    grade = int(input(f"Insert {name}'s grade: "))
    grades.append(grade)

print(f"Student names: {names}, total {len(names)}")
print(f"Grades average: {sum(grades)/len(grades)}")