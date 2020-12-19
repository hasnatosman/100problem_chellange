
"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""

# hints: factorial algorithm

# using function...........................................

def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)


x = int(input("Enter a number: "))
print(fact(x))

# using while................................................

n = int(input('Enter another number: '))
facto = 1
i = 1
while i <= n:
    facto = facto * i
    i = i + 1
print(facto)

# using for loop............................................

n = int(input('Enter a number: '))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(factorial)

# using lambda..............................................

n = int(input('Enter a number :'))


def shortFact(x): return 1 if x <= 1 else x * shortFact(x - 1)


print(shortFact(n))
