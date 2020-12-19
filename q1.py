"""
question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 between 2000 and 3200 (both included).The numbers obtained should be printed in
 a comma-separated sequence on a single line.

"""
# hints: Consider use range(#begin, #end) method.


for i in range(2000, 3200):
    if (i % 5 != 0) and (i % 7 == 0):
        print(i, end=',')
        i += 1
print('\b')
"""
using generator and list comprehension

print(*(i for i in range (2000, 3200) if i % 5 != 0 and i % 7 ==0), sep= ',')
"""
