'''
請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
a. 必須至少八個字元。
b. 只包含英文字母和數字。
c. 至少要有一個大寫英文字母。
d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】。

'''

pw = input('請輸入一個串密碼(至少八位字元,並包含英文及數字,其中一個英文字需大寫):')
b=0
for i in range(len(pw)):
    if pw[i].isupper(): #isupper()判斷字串中所有的字母是否都為大寫。
        b = 1
if b == 1 and len(pw) >=8 and pw.isalnum(): #isalnum判斷字符串是否包含字母數字字符。
        print('valid password')
else:
        print('Invalid password')
