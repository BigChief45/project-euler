## Jaime Alvarez -- October 2016

=begin
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

=end

require 'prime'

def truncatable?(n)
  # Truncate from left to right
  a = n.to_s
  while a.size > 0 do
    return false unless a.to_i.prime?
    a.chop!
  end
  
  # Truncate from right to left
  a = n.to_s
  while a.size > 0 do
    return false unless a.to_i.prime?
    a.slice!(0)
  end
  
  return true
end

answer_primes = []

Prime.each do |num| 
  answer_primes << num if truncatable?(num) && ![2, 3, 5, 7].include?(num)
  break if answer_primes.size >= 11
end

puts "Truncatable Primes: #{answer_primes}"
puts "Answer: #{answer_primes.inject(:+)}"