#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:31:20 2020

@author: michael
"""

# increasing numbers 
def task1(num):
    for i in range(1, num + 1):
        print(i, end = " ")

# decreasing numbers
def task2(num):
    for i in range(num, 0, -1):
        print(i, end = " ")

# n quantity of '*'     
def task3(n):
    for i in range(0, n):
        print("*", end = " ")

# filled square
def task4(side):
    for i in range(0, side):
        for j in range(0, side):
            print("*", end = " ")
        print()
        
# filled triangle 1
def task5(height):
    for i in range(0, height):
        for j in range(0, i + 1):
            print("*", end = " ")
        print()

# filled triangle 2
def task6(height):
    for i in range(height, 0, -1):
        for j in range(0, i):
            print("*", end = " ")
        print()
        
# filled triangle 3
def task7(height):
    for i in range(1, height + 1):
        for j in range(0, height - i):
            print(" ", end = " ")
        for j in range(0, i):
            print("*", end = " ")
        print()

# filled triangle 4
def task8(height):
    for i in range(height, 0, -1):
        for j in range(0, height - i):
            print(" ", end = " ")
        for j in range(0, i):
            print("*", end = " ")
        print()

# pyramid
def task9(height):
    for i in range(1, height + 1):
        for j in range(0, height - i):
            print(" ", end = "")
        for j in range(height - i, height):
            print("*", end = " ")
        print()
    
# inverted pyramid
def task10(height):
    for i in range(height, 0, -1):
        for j in range(0, height - i):
            print(" ", end = "")
        for j in range(0, i):
            print("*", end = " ")
        print()

# triangle of numbers 1
def task11(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()

# triangle of numbers 2      
def task12(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(i, end = " ")
        print()
        
# triangle of numbers 3    
def task13(height):  
    for i in range(1, height + 1):
        for j in range(i, 0, -1):
            print(j, end = " ")
        print()
        
# triangle of numbers 4
def task14(height):
    for i in range(0, height):
        for j in range(height - i, height + 1):
            print(j, end = " ")
        print()

# pyramid of numbers 1
def task15(height):
    for i in range(height, 0, -1):
        for j in range(1, i):
            print(end = " ")
        for j in range(0, height - i + 1):
            print(i, end = " ")
        print()
        
# pyramid of numbers 2
def task16(height):
    for i in range(1, height + 1):
        for j in range(1, i):
            print(end = " ")
        for j in range(1, height - i + 2):
            print(j, end = " ")
        print()

# succession 1
def task17(num):
    for i in range(0, num):
        if i % 2 == 0:
            print("*", end = " ")
        else:
            print("#", end = " ")

# succession 2           
def task18(num):
    for i in range(1, num + 1):
        if i % 3 == 1:
            print("*", end = " ")
        elif i % 3 == 2:
            print("#", end = " ")
        else:
            print("@", end = " ")

# succession 3
def task19(num):
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i, end = " ")
        else:
            print("$", end = " ")
   
# succession 4            
def task20(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            print("*", end = " ")
        else:
            print(i ** 2, end = " ")

# triangle of numbers 5
def task21(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j % 2, end = " ")
        print()
        
# square of numbers 1
def task22(side):
    for i in range(1, side + 1):
        for j in range(1, side + 1):
            if i == j:
                print(i, end = " ")
            else:
                print("0", end = " ")
        print()
        
# triangle of symbols 1
def task23(height):  
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            if i % 2 == 1:
                print("*", end = " ")
            else:
                print("#", end = " ")
        print()

# triangle of symbols 2
def task24(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            if j % 3 == 1:
                print("*", end = " ")
            elif j % 3 == 2:
                print("#", end = " ")
            else:
                print("@", end = " ")
        print()

# pyramid of numbers and symbols
def task25(height):
    for i in range(1, height + 1):
        for j in range(0, height - i):
            print(end = " ")
        for j in range(1, i + 1):
            if i % 2 == 1:
                print("*", end = " ")
            else:
                print(j, end = " ")            
        print()

# square of numbers 2
def task26(side):
    for i in range(1, side + 1):
        for j in range(i, side):
            print("1", end = " ")
        for j in range(1, i + 1):
            print(i, end = " ")
        print()
        
# skate ramp
def task27(num):
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end = " ")
        print()
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()

# hourglass
def task28(num):
    for i in range(1, num + 1):
        for j in range(1, i):
            print(end = " ")
        for j in range(i, num + 1):
            print(j, end = " ")
        print()
    for i in range(num, 0, -1):
        for j in range(1, i):
            print(end = " ")
        for j in range(i, num + 1):
            print(j, end = " ")
        print()
        
# pyramid of symbols 1
def task29(height):
    for i in range(1, height + 1):
        for j in range(0, (2*height - 2 - 2*(i - 1))):
            print(end = " ")
        for j in range(0, (i - 1) * 2 + 1):
            print("*", end = " ")
        print()
            
# stairs 1
def task30(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end = "")
        for j in range(i - 1, 0, -1):
            print(j, end = "")
        print()
        
# stairs 2
def task31(height):
    for i in range(1, height + 1):
        for j in range(i, height + 1):
            print(j, end = "")
        for j in range(height - 1, i - 1, -1):
            print(j, end = "")
        print()

# pyramid of symbols 2
def task32(height):
    for i in range(1, height + 1):
        for j in range(0, i):
            print("*", end = "")
        print()
    for i in range(height - 1, 0, -1):
        for j in range(0, i):
            print("*", end = "")
        print()        
        
# succession 5
def task33(num):        
    for i in range(-num, num + 1):
        print(i, end = " ")

# succession 6
def task34(num):
    for i in range(-num, num + 1):
        print(abs(i), end = " ")
        
# succession 7
def task35(num):
    for i in range(-num + 1, num):
        print(num - abs(i), end = " ")    

# succession 8
def task36(num):
    for i in range(-num + 1, num):
        n = num - abs(i)
        if n % 2 == 1:
            print(n, end = " ")
        else:
            print("@", end = " ")

# succession 8
def task37(num):
    for i in range(-num + 1, num):
        if i < 0:
            print( (2*abs(i) + 1)*2, end = " ")
        elif i == 0:
            print(i, end = " ")
        else:
            print((2*i + 1), end = " ")

# succession 9
def task38(num):
    for i in range(1, num + 1):
        print(chr(i + 64), end = " ")
        
# succession 10
def task39(num):
    for i in range(num, 0, -1):
        print(chr(i + 64), end = " ")

# succession 11
def task40(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            print(chr(i + 64), end = " ")
        else:
            print(chr(i + 64).lower(), end = " ")
            
# pyramid of numbers 3
def task41(height):
    for i in range(-height + 1, height):
        n = height - abs(i)
        for j in range(1, n + 1):
            print(n, end = "")
        print()
        
# pyramid of numbers 4
def task42(height):
    for i in range(-height + 1, height):
        n = height - abs(i)        
        for j in range(-n + 1, n):
            n = height - abs(j)
            print(n, end = "")
        print()
      
# pyramid of numbers 5
def task43(height):
    for i in range(-height + 1, height):
        n = height - abs(i)
        for j in range(1, n + 1):
            print(j, end = "")
        print()

# diamond of numbers
def task44(diag):
    for i in range(1, diag * 2):
        n = abs(diag - i)
        for j in range(0, n):
            print(end = " ")
        for j in range(1, diag - n + 1):
            print(j, end = " ")
        print()
        
# pyramid of numbers 6
def task45(height):
    for i in range(1, height + 1):        
        for j in range(i, height):
            print(end = " ")
        for j in range(-i + 1, i):
            print(i - abs(j), end = "")
        print()
        
task42(4)        
    