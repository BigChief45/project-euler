### Jaime Alvarez - March 2016

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

** See numbers.txt **
"""

import sys

numbers = []

# Open the file and read each number and store it
numbers = [line.rstrip('\n') for line in open('numbers.txt')]

# Sum the numbers
total_sum = 0

for i in numbers:
    total_sum += int(i)
    
print "Sum = ", total_sum

# Get the 1st ten digits
print "First 10 digits of the sum: "
count = 0
for i in str(total_sum):
    if count >= 10:
        break
    sys.stdout.write(i)
    count += 1 

print
