# Alex Hicks (awh4kc)

number = int(input('Enter an integer: '))
number1 = number + 1

if number > 3999 or number < 1:
    print("Input must be between 1 and 3999")
else:
    roman = ""

    while number1 > 1000:
        roman += 'M'
        number1 -= 1000
    while number1 > 900:
        roman += 'CM'
        number1 -= 900
    while number1 > 500:
        roman += 'D'
        number1 -= 500
    while number1 > 400:
        roman += 'CD'
        number1 -= 400
    while number1 > 100:
        roman += 'C'
        number1 -= 100
    while number1 > 90:
        roman +='XC'
        number1 -= 90
    while number1 > 50:
        roman +='L'
        number1 -= 50
    while number1 > 40:
        roman +='XL'
        number1 -= 40
    while number1 > 10:
        roman += 'X'
        number1 -= 10
    while number1 > 9:
        roman += 'IX'
        number1 -= 9
    while number1 > 5:
        roman += 'V'
        number1 -= 5
    while number1 > 4:
        roman += 'IV'
        number1 -= 4
    while number1 > 1:
        roman += 'I'
        number1 -= 1

    print("In roman numerals, " + str(number) + " is " + roman)

#I talked over ideas with my friend Andrew Walsh (abw9yd)
