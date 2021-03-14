# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:12:26 2021

@author: user
"""

"""
最小是1, 最大是100
ex:
答案是61
猜71,顯示請輸入1~71之間的值
猜20,顯示請輸入21~70之間的值
如果猜錯達5次，離開
"""

# 猜',m,'-',M,'之間的整數:
#print('猜%d-%d之間的整數:'%(m,M))
    
import random

m = 1
M = 100
ans = random.randint(m, M)
guess = 0
freq = 1   #次數
while ans != guess :
    if freq <= 5 :   
        print('猜%d-%d之間的整數:'%(m,M), end = '')
        guess = int(input())
        
        while (guess < m) or (guess > M):
            guess = int(input('輸入錯誤，重新輸入:'))
        
        if guess > ans:
            M = guess-1
            print('猜小一點!')
            print()
        if guess < ans:
            m = guess+1
            print('猜大一點')
            print()
        if guess == ans:
            print('猜對了!')
    else:
        print("猜錯達5次，下次再接再厲!")
        break
    freq +=1 
    
print('遊戲結束!')