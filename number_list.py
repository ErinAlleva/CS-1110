# Alex Hicks (awh4kc)

x = int(input("What is number 1?"))
y = int(input("What is number 2?"))
z = int(input("What is number 3?"))
a = int(input("What is number 4?"))
b = int(input("What is number 5?"))

numbers = [x, y, z, a, b]

print("You entered:"), print(numbers[0:])

print("The average is:"), print(sum(numbers[0:])/int(len(numbers)))

print("The range is:"), print(max(numbers[0:]) - min(numbers[0:]))

c = int(input("Which item do you want to remove?"))

numbers.remove(c)

print("The new list has the following values:"), print(numbers[0:])

print("The average is:"), print((sum(numbers[0:])/4))

print("The range is:"), print(max(numbers[0:]) - min(numbers[0:]))

