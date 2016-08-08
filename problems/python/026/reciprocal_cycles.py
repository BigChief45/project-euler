### Jaime Alvarez - March 2016

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

import math

d = 10
recurring_digits = 0

for i in range(2, d+1):
    a = 1.00 / i
    print "1/%s = %s" % (i, a)
    
    # Get the dividend part
    dividend = str(math.modf(a))
    
    # loop through each digit of the dividend
    # Dictionary that checks for recurring cycles.
    # Key: starting cycle digit's position
    # Value: digit cycle's 1st digit
    recurring_cycles = {}
    cycle_pos = 0
    
    for digit in dividend:
        if ( digit in recurring_cycles[cycle_pos] ):
            recurring_cycles[cycle_pos].join(digit)
        
        # Check if digit is inside dictionary
        
        
        # Add the digit to the dictionary by concatenating
        recurring_cycles[cycle_pos] = recurring_cycles[cycle_pos].join(digit)
        
        