'''
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

#ejemplo [i*2 for i in range(1, 101) if i % 2 == 0]
'''

number = []
for i in range(1, 11):
    if i % 2 == 0:
        number.append(i * 2)

print(number)

numbers_v2 = [i*2 for i in range(1, 11)  if i % 2 == 0]
print(numbers_v2)