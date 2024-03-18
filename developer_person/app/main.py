import mod

data = [
    {
        'country' : 'Colombia',
        'Population' : 500
    },
    {
        'country' : 'Bolivia',
        'Population' : 300
    }
]

def run():
    keys, values = mod.get_population()
    print(keys, values)

    country = input('type Country => ')

    result = mod.get_population(data, country)
    print(result)

if __name__ == '__main__':
    run()