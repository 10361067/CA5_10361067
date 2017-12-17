# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:54:43 2017

@author: Kristina Kavanagh
"""
list1 = [3, 4, -2, 5, 9]
#defining sum function#
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum(list1))

#subtract function#
from operator import sub

a = [4, 8, 4]
b = [2, 3, -3]
sub_result = map(sub, a, b)
print sub_result

#division function#
list1 = [3, 4, -2, 5, 9]
list2 = [1, 3, 5, 7, 8]
result = []
result = [list1[i]/ list2[i] for i in range(len(list1))]
print result

#multiplication#
from operator import mul
list_1 = [2, 4, 5, 7, 8]
list_2 = [2, 3, 5, 6, 9]
result_mult = map(mul, list_1, list_2)
print result_mult

#defining square function#
def square(x):
    return x*x
list2 = [1, 3, 5, 7, 8]
squares = map(square, list2)
squares_as_strings = map(str, squares)
print(','.join(squares_as_strings))

#factorial function#
my_list = [2, 4, 6, 8]
for item in my_list:
    fact = 1
    for number in range(1,item+1):
        fact = fact * number
    print fact