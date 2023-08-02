"""
Create a python script:
create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console
Each line of code should be commented with description.
"""
# a is a random number fom 0 to 1000
from random import randint

j = 0
# b is the list to save the 100 numbers of a
b = []
# save a to b list
while j < 100:
    a = randint(0, 1000)
    # print(a)
    b.append(a)
    j += 1
# print original list
print(b)

# sorted list :from min to max
# iterate each value of list length of list times
# each time find the min value of the remaining values
for i in range(len(b)):
    for j in range(len(b) - 1):
        if b[j] > b[j + 1]:
            tmp = b[j + 1]
            b[j + 1] = b[j]
            b[j] = tmp
# print sorted list
print(b)
# find even and odd numbers of list
# and calculate their counts and sums
evenSum = 0
evenCount = 0
oddSum = 0
oddCount = 0
for k in range(len(b)):
    if (b[k] % 2) == 0.0:
       # print(b[k] % 2)
        evenSum += b[k]
        evenCount += 1
    else:
       # print(b[k] % 2)
        oddSum += b[k]
        oddCount += 1

# calculate average of even and odd numbers
# and print them if exits

if evenCount != 0:
    avgEven = evenSum / evenCount
    print('Average of even numbers is :')
    print(avgEven)
else:
    print('No even numbers this time.')
if oddCount != 0:
    avgOdd = oddSum / oddCount
    print('Average of odd numbers is :')
    print(avgOdd)
else:
    print('No odd numbers this time.')
