import functools

numbers = [1,2,3,4,5,6,7,8,9]

def acumulador(counter, item):
    print(counter)
    print(item)
    return counter + item

 
result = functools.reduce(lambda x, item: x + item, numbers)

print(result)