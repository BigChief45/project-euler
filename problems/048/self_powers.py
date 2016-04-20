### Jaime Alvarez - April 2016

"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

import sys

power_sum = 0

# Get the sum of the powers
for i in xrange(1, 1000+1):
    power_sum += i**i

print "Last 10 digits of the series: "

power_sum = str(power_sum)
# Find the last 10 digits
for i in xrange(len(power_sum) - 10, len(power_sum)):
    sys.stdout.write(power_sum[i])

print