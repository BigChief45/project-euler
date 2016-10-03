## Jaime Alvarez -- October 2016

=begin
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
=end

require 'prime'

def pandigital?(num)
  digits = num.to_s.size
  for i in 1..digits do
    return false unless num.to_s.include?(i.to_s)
  end
  
  return true
end

largest_pandigital_prime = 0

Prime.take(1000000).each do |prime|
  largest_pandigital_prime = prime if pandigital?(prime) && prime > largest_pandigital_prime
end

puts "Largest n-digit pandigital prime: #{largest_pandigital_prime}"