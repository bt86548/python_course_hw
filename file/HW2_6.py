d = {}
while True:
    k = input('key:')
    if k =='end':
        break
    d[k] = input('value:')

sc = input('search key:')
print(sc in d.keys())