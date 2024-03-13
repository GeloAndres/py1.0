items = [
    {
        'producto': 'camisa',
        'price' : 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]


#resultado una lista con los precios, [100, 300, 200]
prices = list(map(lambda item: item['price'], items))
print(prices)

def add_imp(item):
    item['impuesto'] = item['price'] * 0.19
    return item

prices_imp = list(map(add_imp, items))
print(prices_imp)
print(items)

##importante saber que aqui la lista items fue mutada por la funcion add_imp, le agrego valores a la lista 
#laterando sus valores originales y modificandola