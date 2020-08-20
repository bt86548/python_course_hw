'''
請撰寫一程式，要求使用者輸入一個長度為6的字串，
將此字串分別置於10個欄位的寬度的左邊、
中間和右邊，並顯示這三個結果，左右皆以直線 |（Vertical bar）作為邊界。
'''

enter = input('請輸入一個長度為6的字串')
print('|%s|'%enter.ljust(10))
print('|%s|'%enter.center(10))
print('|%s|'%enter.rjust(10))


