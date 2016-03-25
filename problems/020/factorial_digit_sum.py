### Jaime Alvarez - March 2016

"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

n = 100
factorial = 1

for i in range(n, 0, -1):
    factorial *= i
    
print "Factorial = ", factorial

factorial = str(factorial)

factorial_sum = 0
for i in factorial:
    factorial_sum += int(i)
    
print "Factorial sum = ", factorial_sum