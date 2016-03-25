### Jaime Alvarez - March 2016

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import math

power = 1000

# Calculate the exponential result
r = math.pow(2, power)

# Convert to integer
r = int(r)

# Conver to string
r = str(r)

# Iterate over each digit and sum them
digit_sum = 0

for digit in r:
    digit_sum += int(digit)
    
    
print "Sum of digits of 2^%s = %s" % (power, digit_sum)