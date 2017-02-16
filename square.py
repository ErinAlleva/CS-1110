# Alex Hicks (awh4kc)

square = [[1,2,3],[4,5,6],[7,8,9]]

row_to_print = ""

for row in square:
    for col in row:
        row_to_print += str(col) + "\t"
    print(row_to_print)
    row_to_print = ""

