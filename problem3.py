# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 06:56:43 2023

Solution to
https://projecteuler.net/problem=1

@author: EW
"""

primeFactor=13195
# primeFactor=600851475143
fact=5
lastfact=fact
while fact<30: #primeFactor:
    lastfact=fact
    for i in range(fact):
        if fact%(i+2)==0:
            fact+=1

solution=lastfact
print('The solution to problem 3 is %d' % solution)