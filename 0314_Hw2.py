# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:07:48 2021

@author: user
"""

"""
使用者輸入一個範圍的整數 (若1~10，rang(1,11))
1.求4的倍數有那些?
2.哪些是質數?
"""

num = int(input("輸入一個整數:"))

print( '4的倍數有：' )
for i in range(1,num+1):
    if i % 4 == 0:
        print( i )
        
print()
print( '質數：' )  
for a in range(2,num+1):  
    if a ==2 :
        print(a) 
    else:
        for b in range(2,a):
            if a % b == 0:
                break
            elif b == a-1:
                print(a)
  
        


