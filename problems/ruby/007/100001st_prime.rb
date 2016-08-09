### Jaime Alvarez - August 2016

=begin
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
=end

require 'prime'

puts "Answer: %d" % Prime.take(10001).last