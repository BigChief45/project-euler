## Jaime Alvarez -- September 2016

=begin

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

=end

# NOTE: This algorithm works for the problem's question case. However, it does not work with the base case provided
# (41 as the consecutive prime sum). This is because the algorithm uses shift method to discard the 1st elements
# from the comparison list. This means that it will discard a necessary element to reach the '41' base case solution.
# If 'pop' method is used, the base case will work. But the later cases will no longer work.

require 'prime'

CEIL = 100
primes = Prime.take_while { |i| i < CEIL }

sum = 0
terms = []

# Find the all the primes whose sum does not exceed CEIL
primes.each do |prime|
  if sum + prime < CEIL
    sum += prime
    terms << prime
  end
end

largest_sum_seq = []
until terms.empty? do
  term_sum = terms.inject(:+)
  #puts "#{terms.inspect} = #{term_sum} - #{primes.include?(terms.inject(:+))}"
  largest_sum_seq = terms.dup if primes.include?(term_sum) && term_sum > largest_sum_seq.inject(0, :+) && terms.size > largest_sum_seq.size
  terms.shift
end

puts "Largest sum: #{largest_sum_seq.inject(:+)}"