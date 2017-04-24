## Jaime Alvarez -- October 2016

=begin
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
=end

# Composite Number: A composite number is a positive integer that can be formed by multiplying together two smaller positive integers.
# Equivalently, it is a positive integer that has at least one divisor other than 1 and itself.
# Every positive integer is composite, prime, or the unit 1, so the composite numbers are exactly the numbers that are not prime and not a unit.

require 'prime'

def odd_composites
  Enumerator.new do |y|
    i = 2
    loop do
      y << i if !i.prime? && i.odd?
      i += 1
    end
  end
end


def golbach?(n)
  # First, find the primes
  primes_below_n = Prime.take_while { |i| i < n }

  # Test each prime with the sum of twice a square
  primes_below_n.each do |prime|
    i = 1
    loop do
      sum = prime + (2 * i**2)
      if sum == n
        return true
      elsif sum > n
        break
      end
      i += 1
    end
  end

  return false
end

odd_composites.each do |c|
  unless golbach?(c)
    puts "the smallest odd composite that cannot be written as the sum of a prime and twice a square is: #{c}"
    break
  end
end