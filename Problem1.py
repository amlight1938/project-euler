## Project Euler problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6,9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

import time


num = 1000
m1 = 3
m2 = 5


## method 1

start = time.perf_counter()

sum = 0
iter = 1

for i in range(num):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print("Answer: ", sum)
end = time.perf_counter()
passed = end - start
print("time 1: ", passed)

del iter



## method 2

start2 = time.perf_counter()

sum2 = 0
iter = 1

while True:
    curr1 = iter * m1
    curr2 = iter * m2
    currLCM = iter * m1*m2  # Least common multiplier
    
    if curr1 >= num and curr2 >= num and currLCM >= num:
        break

    if curr1 < num and curr1 % (m1*m2) != 0:
        sum2 += curr1
    
    if curr2 < num and curr2 % (m1*m2) != 0:
        sum2 += curr2
    
    if currLCM < num:
        sum2 += currLCM
    
    iter += 1

print("Answer: ", sum2)
end2 = time.perf_counter()
passed2 = end2 - start2
print("time 2: ", passed2)

print("time ratio method 1/method 2: ", passed/passed2)