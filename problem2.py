# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 06:56:43 2023

Solution to
https://projecteuler.net/problem=1

@author: EW
"""
i=0
fib=[1,2]
solution=2
while fib[-1]<4e6:
    nextVal=fib[i]+fib[i+1]
    if nextVal%2==0:
        solution+=nextVal
    fib[0]=fib[-1]
    fib[-1]=nextVal


print('The solution to problem 1 is %d' % solution)