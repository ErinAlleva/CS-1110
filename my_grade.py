# Alex Hicks (awh4kc)

my_grade = int(input("What is your grade?: "))

if my_grade > 100 or my_grade < 0:
    print("What class are you in?")

if my_grade >= 98:
    print("A+")
elif my_grade >= 93:
    print("A")
elif my_grade >= 90:
    print("A-")
elif my_grade >= 87:
    print("B+")
elif my_grade >= 83:
    print("B")
elif my_grade >= 80:
    print("B-")
elif my_grade >= 77:
    print("C+")
elif my_grade >= 73:
    print("C")
elif my_grade >= 70:
    print("C-")
elif my_grade >= 67:
    print("D+")
elif my_grade >= 63:
    print("D")
elif my_grade >= 60:
    print("D-")
else:
    print("F")
