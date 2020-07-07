# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:36:35 2020

@author: MADCAT
"""

while True:
    num = input("Please input an integer:")

    chk_list = {",", "."}

    s = set(map(chr, range(*map(ord, 'az'))))

    if "-" in set(num) :
        print("Please enter a positive number")
        continue
    
    elif set(num) & s == set(num):
        print("Do not use any entries other than numeric values")
        continue
    
    elif (set(num) & chk_list == {"."}) or (set(num) & chk_list == {","}) :
        print("Please enter an integer number")
        continue
    
    else :
        ara = list(num)
        top = 0
        
        for i in ara:
            top += (int(i) ** len(num))
    
        if int(num) == top :
            print(f"{num} is an Armstrong number")
            
        else:
            print(f"{num} is not an Armstrong number")
    break
            



