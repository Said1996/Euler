# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:35:08 2019

@author: Ami
"""

num1 = 0
num2 = 1
num3 = 0
total = 0
while num3 < 4000000:
    num3 = num1 + num2 
    num1 = num2 
    num2 = num3
    if num3 % 2 == 0:
        total += num3
print(total)

