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

#aqui punto de interes!!
def add_imp(item):
    new_items = item.copy()
    new_items['impuesto'] = new_items['price'] * 0.19
    return new_items

prices_imp = list(map(add_imp, items))
print(prices_imp)
print(items)