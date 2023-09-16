# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 06:56:43 2023

Solution to
https://projecteuler.net/problem=1

@author: EW
"""

solution=sum([e for e in list(range(1000)) if (e%3==0 or e%5==0)])

print('The solution to problem 1 is %d' % solution)