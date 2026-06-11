#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 05:25:33 2026

@author: s-a-r
"""
import random
def flip_a_coin():
    if random.random()<0.5:
        return 'Head'
    else:
        return 'Tails'
count_head=0
print('how many times you wanna flip?')
x=int(input())
for i in range(x):
    result=flip_a_coin()
    if result=='Head':
        count_head=count_head+1
print(f'Heads ratio= {(count_head/x)*100:1.2f} %')
count_Tails=x-count_head
print(f'Tails ratio= {(count_Tails/x)*100:1.2f} %')