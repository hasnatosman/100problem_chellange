def get_sum(sums):
    sum = 0
    for i in sums:
        sum = sum + i
    return sum


sums = [2, 4, 6]
total = get_sum(sums)

print('Sum of the numbers in list is: ', total)
