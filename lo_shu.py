# Alex Hicks (awh4kc)
# Kevin Dela Merced (krd5sv)

test = True

num = input("Numbers: ").split( )
list1 = num[:3]
list2 = num[3:6]
list3 = num[6:9]

list4 = [num[0], num[3], num[6]]
list5 = [num[1], num[4], num[7]]
list6 = [num[2], num[5], num[8]]

list7 = [num[0], num[4], num[8]]
list8 = [num[2], num[4], num[6]]

list7 = list(map(int, list7))
list8 = list(map(int, list8))

diagonal = [list7, list8]

list4 = list(map(int, list4))
list5 = list(map(int, list5))
list6 = list(map(int, list6))

columns = [list4, list5, list6]

list1 = list(map(int, list1))
list2 = list(map(int, list2))
list3 = list(map(int, list3))

rows = [list1, list2, list3]

print("You entered: ")
for a in range(3):
    for b in range(3):
        print(rows[a][b], end=" ")
    print()

for x in rows:
    xadd = sum(x)
    if xadd != 15:
        print(str(x) + " fails the test!")
        test = False

for y in columns:
    yadd = sum(y)
    if yadd != 15:
        print("Column " + str(columns.index(y)) + " fails the test!")
        test = False

for z in diagonal:
    zadd = sum(z)
    if zadd != 15:
        print("Diagonal " + str(diagonal.index(z)) + " fails the test!")
        test = False

if test == False:
    print("This is not a Lo Shu Magic Square!")
if test == True:
    print("This is a valid Lo Shu Magic Square!")