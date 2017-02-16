# Alex Hicks (awh4kc)

#Old MacDonald Had a Farm

animals = ['pig', 'cow', 'dog', 'sheep', 'squid', 'chupacabra']
sounds = ['oink', 'moo', 'woof', 'baa', 'bloop', 'mrrrrooowwwww']

# for i in range(len(animals)):
#     print("Old MacDonald had a farm, E I E I O")
#     print("And on that farm he had a", animals[i], ", E I E I O")
#     print("With a", sounds[i], sounds[i], "here and a", sounds[i], sounds[i], "there")
#     print("Here a", sounds[i], "there a", sounds[i], "everywhere a", sounds[i], sounds[i])
#     print("Old MacDonald had a farm, E I E I O")
#     print()
#
# i = 0
#
# while i < len(animals):
#     print("Old MacDonald had a farm, E I E I O")
#     print("And on that farm he had a", animals[i], ", E I E I O")
#     print("With a", sounds[i], sounds[i], "here and a", sounds[i], sounds[i], "there")
#     print("Here a", sounds[i], "there a", sounds[i], "everywhere a", sounds[i], sounds[i])
#     print("Old MacDonald had a farm, E I E I O")
#     print()
#     i += 1
#
# while len(animals) > 0:
#     print("Old MacDonald had a farm, E I E I O")
#     print("And on that farm he had a", animals[0], ", E I E I O")
#     print("With a", sounds[0], sounds[0], "here and a", sounds[0], sounds[0], "there")
#     print("Here a", sounds[0], "there a", sounds[0], "everywhere a", sounds[0], sounds[0])
#     print("Old MacDonald had a farm, E I E I O")
#     print()
#     del animals[0]
#     del sounds [0]

square = [[1,2,3], [4,5,6], [7,8,9]]
sum = 0
for i in range(len(square)):
    sum += square[i][i]

print(sum)

total_sum = 0
for i in range(len(square)):
    for j in range(len(square)):
        total_sum += square[i][j]

print(total_sum)

total_sum = 0
for row in square:
    for item in row:
        total_sum += item

print(total_sum)

