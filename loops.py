# Alex Hicks (awh4kc)

x = 0
while x < 5:
    print(x)
    x += 1
#Then goes to here

word = ""
while not word == "stop":
    word = input("Give me a word (stop to stop) : ")
    print("You said: " + word)


number = -1
while number < 1 or number > 100:
    number = int(input("Gimme number between 1 and 100: "))
print(number)

number = -1
while number not in range(1, 101):
    number = int(input("Gimme number between 1 and 100: "))
print(number)

for i in range(0,4): # range is [0,1,2,3] range is effectively a list
    print(i)

students = ['Mark', 'Colin', 'Sammy', 'Sarah', 'Laurie']

for student in students:
    print(student)

for i in range(0, 20, 2): # 2 is the interval
    print(i)

for i in range(100, 20, -5): # range(start, stop, interval)
    print(i)

