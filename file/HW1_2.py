min = float(input('請輸入分鐘:'))
sec = float(input('請輸入秒數:'))
km = float(input('請輸入公里數:'))

j = km/1.6/((min*60+sec)/3600)


print('時速為:' + '%.1f'%j + 'miles/hrs')