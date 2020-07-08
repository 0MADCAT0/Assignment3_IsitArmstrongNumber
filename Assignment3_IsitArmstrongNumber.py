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
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    
    elif set(num) & s == set(num):
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    
    elif (set(num) & chk_list == {"."}) or (set(num) & chk_list == {","}) :
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
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
            



