'''
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。
若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。
'''

SSN = list(input().split("-")) #split通過指定分隔符對字串進行切片，如果參數num有指定值，則分隔num+1個子字符串
b=0
for i in range(len(SSN)):
  if SSN[i].isdigit()==False: #方法檢查字符串是否包含數字(全由數字組成)。
    print("Invalid SSN")
    b+=1
    break
if b==0:
  print("Valid SSN")