### Jaime Alvarez - August 2016

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

import sys

def d(n):
    divisors_sum = 0
    for i in xrange(1, n):
        # Check if i divides n evenly
        if n % i == 0 : divisors_sum += i
        
    return divisors_sum
    
if __name__ == '__main__':
    # Evaluate the sum of all amicable numbers under 10,000
    
    amicable_numbers = []
    amicable_sum = 0
    for a in xrange(1, 10000):
        d_a = d(a)
        d_b = d(d_a)
        
        # Check that a != b
        if a != d_a :
            # Check if they are an amicable pair
            if (a == d_b) and (d_a == d(d_b)):
                amicable_numbers.append(a)
                amicable_numbers.append(d_a)
            
    
    # Remove duplicates
    amicable_numbers = set(amicable_numbers)
    
    # Return the sum
    print "Sum of amicable numbers below 10,000: ", (sum(amicable_numbers))