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

# pyramid of numbers
def task15(height):
    for i in range(height, 0, -1):
        for j in range(1, i):
            print(end = " ")
        for j in range(0, height - i + 1):
            print(i, end = " ")
        print()

            