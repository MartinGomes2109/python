items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 120
    },
    {
        'product': 'camisa',
        'price': 150
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes, items))
print('lista nueva')
print(new_items)
print('lista vieja')
print(items)