### Jaime Alvarez - March 2016

"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

start = 13

total_terms = 0
longest_starting_number = 0

while start < 1000000:
    n = start
    n_terms = 0
    while n >= 1:
        n_terms += 1
        
        # Check if it's 1, end
        # Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1
        if n == 1:
            break
        
        #  Check if it's odd or even
        if n % 2 == 0:
            # Even
            n = n / 2
        else:
            # It's odd
            n = 3 * n + 1
    
    if n_terms > total_terms:
        total_terms = n_terms
        longest_starting_number = start
        
    start += 1

print "Longest starting number is: ", longest_starting_number
print "Total Terms = ", total_terms