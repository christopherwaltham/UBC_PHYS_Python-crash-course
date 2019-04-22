#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:42:50 2019

@author: mkals
"""


def sumOfNaturalNumbers():
    return sum(range(100))


def sCountFixed():
    string = 'UBC Physics and Astronomy'
    count = 0
    for c in string:
        if c == 's':
            count += 1
    return count

def sCountWithArgument(string):
    count = 0
    for c in string:
        if c == 's':
            count += 1
    return count

def charCount(string, char):
    return sum(c == char for c in string)

def printPrimes(upperLimit):
    primes = []
    
    for i in range(1, upperLimit):
        prime = True
        for j in range(2, i):
            if i%j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
            
    return primes

def mode(values):
    
    frequency = {} # dictionary
    for val in values:
        if val in frequency:
            frequency[val] += 1
        else:
            frequency[val] = 1
    return max(frequency, key=frequency.get)



print(sumOfNaturalNumbers())
print(sCountFixed())
print(sCountWithArgument('UBC Physics and Astronomy'))
print(charCount('UBC Physics and Astronomy', 's'))
print(printPrimes(100))
print(mode([1,2,3,4,5,6,4,3,2,2]))
