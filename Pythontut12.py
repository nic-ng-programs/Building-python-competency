'''
import time
start = time.time()
my_value = 1
n = 100
for i in range(n):
    for j in range (n):
        my_value += j
    my_value *= 2
print(time.time()-start)

start1 = time.time()
my_value1 = 1
n = 100
for i in range(n):
    for j in range (n):
        my_value1 *= 2
    my_value1 *= j
print(time.time()-start1)
'''

def average(my_list):
    big = 0
    for x in my_list:
        big += x
    ard = big/len(my_list)
    print(ard)

average([12,34,56,78,11,23,66,23,40,6.7])