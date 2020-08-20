str_c = '''this is 
a mutiple
string'''

print(str_c)

list_a = [10,20,30]
str_a = ''
for item in list_a:
    str_a  = str_a + ' ' +str(item)
    print(str_a)

dict_a = {0:'apple',1:'orange',2:'mango'}
for i in range(len(dict_a)):
    print("item",i,":"+(" "+dict_a[i]))

str_t = "\'This is a python string.\'"
# for i in range(len(str_t)):
    #print("str_t[",i,"]) = " , str_t[i])

print(str_t[1:])
print(str_t[:10])
print(str_t[10:17])
print(str_t[17:])
print(str_t[:10]+str_t[17:])
print(str_t[::3])

str_p = "alicE , jOe , boB , kenT , zoyTsaG"
print(str_p.lower())
print(str_p.upper())
print(str_p.title())

str_t = "python is powerful"
print(str_t.capitalize())

str_s = "Hello"
print('\'' + str_s.rjust(20)+'\'')
print('\'' + str_s.ljust(20)+'\'')
print('\'' + str_s.center(20)+'\'')

str_b = '          @@@@@@@@ python @@@@@@    '
print(str_b.strip().strip('@'))
print('\''+str_b.lstrip()+'\'')

str_p = 'python is easy to learn, and easy to use.'
print(str_p.find('to'))
print(str_p.rfind('to'))

print(str_p.count(('to')))

str_m = str_p.replace('to',' ',str_p.count('to'))

print('to' in str_m)
print(str_m)
print('to' not in str_m)

print(str_p.startswith('python'))
print(str_p.endswith('.'))

str_z = "alice , joe , bob , kent , zoey"
str_r =''
for item in str_z.split(' , '):
    str_r += item[0:-1] +item[-1].upper() + " "
print(str_r)
print(','.join(str_r.split()))