def sqr_sum(num):
    sum = 0

    for i in range(num+1):
        square = (i ** 2)
        sum = sum + square
        print(i, 'Square is: ', square)
    return sum


num = int(input('Enter a number: '))
sum = sqr_sum(num)

print('sum of square numbers is ', sum)