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
    if i % m1 == 0 or i % m2 == 0:
        sum += i

end = time.perf_counter()
print("Method 1 answer: ", sum)
passed = end - start
print("time 1: ", passed)

del iter


## method 2
start2 = time.perf_counter()

x = lambda w: (num - 1)//w
gaussSum = lambda u: u*x(u)*(x(u)+1)/2
ans = gaussSum(m1) + gaussSum(m2) - gaussSum(m1*m2)

end2 = time.perf_counter()
print("Method 2 answer: ", ans)
passed2 = end2 - start2
print("time 2: ", passed2)

