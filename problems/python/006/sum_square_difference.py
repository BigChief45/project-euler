### Jaime Alvarez - March 2016

"""
he sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumSquares(n):
    r = 0
    for i in range(1, n+1):
        r += (i**2)
        
    return r
    
def squareSums(n):
    r = 0
    
    # Im sure there must be a formula to calculate this faster
    for i in range(1, n+1):
        r += i
        
    r = r**2
    
    return r

if __name__ == '__main__':
    n = 100
    
    s = sumSquares(n)
    print "Sum of the squares = ", s
    
    s2 = squareSums(n)
    print "Square of the sums = ", s2
    
    print "Difference = ", (s2 - s)