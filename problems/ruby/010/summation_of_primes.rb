### Jaime Alvarez - August 2016

=begin
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
=end

require 'prime'

answer = Prime.each(2000000).inject(:+)

puts "Answer: %d" % answer