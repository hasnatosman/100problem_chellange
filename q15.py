"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
"""

a = input()
total, tmp = 0, str()  # initialing an integer and empty string

for i in range(4):
    tmp += a  # concatenating 'a' to 'tmp'
    total += int(tmp)  # converting string type to integer type

print(total)
