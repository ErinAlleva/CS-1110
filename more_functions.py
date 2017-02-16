# Alex Hicks (awh4kc)

def void_function(x,y):
    print(x + y)
    return

def return_function(x,y):
    return x + y

# print(void_function(4,6))
# print(return_function(4,7))

def multiple_return(x,y):
    return x + y, x - y

print(multiple_return(8,9))
sum,diff = multiple_return(8,9)
print(sum)
print(diff)

def my_function(name = "Mark", school = "UVa"):
    print(name + " goes to " + school)

my_function()
my_function("Steve")
my_function(school = "VT")
my_function("Ann", "GMU")
my_function(school = "GMU", name = "Ann")

