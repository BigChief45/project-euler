### Jaime Alvarez - August 2016

=begin
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
=end

require 'prime'

n = 600851475143

puts "Largest prime of %d is: %d" % [n, Prime.prime_division(n).flatten(1).max]