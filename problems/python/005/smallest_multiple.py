### Jaime Alvarez - March 2016

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import timeit

start = timeit.default_timer()

digit_start = 1
digit_end = 20

i = 5040
smallest = 0

while True:
    for k in range(digit_start, digit_end + 1):
        if i % k != 0:
            break
    else:
        smallest = i
        break;
    i += 1 

print "Smallest = ", smallest

f = open("answer.txt","a")
f.write("Smallest = " + str(smallest) + "\n")
    
stop = timeit.default_timer()

print "Running time: %s seconds" % (stop - start)

f.write("Running time: " + str(stop - start) + "\n")
f.close()