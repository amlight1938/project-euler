## Project Euler problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6,9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

import time

# params
num = 1000
m1 = 3
m2 = 5

# method 1
def iterativeSolution(num, m1, m2):
    sum = 0

    for i in range(num):

        if i % m1 == 0 or i % m2 == 0:
            sum += i
    return sum

# method 2
def gaussSum(num, m1, m2):
    x = lambda w: (num - 1)//w
    gaussSum = lambda u: u*x(u)*(x(u)+1)/2
    return gaussSum(m1) + gaussSum(m2) - gaussSum(m1*m2)

start1 = time.perf_counter()
print(f"Iterative answer: {iterativeSolution(num, m1, m2)}")
print(f"Ran in {(time.perf_counter() - start1)*1000} ms")
print()

start2 = time.perf_counter()    
print(f"Gause sum answer: {gaussSum(num, m1, m2)}")
print(f"Ran in {(time.perf_counter() - start2)*1000} ms")
print()