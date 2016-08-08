### Jaime Alvarez - August 2016

=begin
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
=end

def palindrome?(n)
  n = n.to_s
  n == n.reverse
end

largest_palindrome = 0
(100...999).each do |i|
  (100...999).each do |k|
    largest_palindrome = i*k if palindrome?(i*k) && i*k > largest_palindrome
  end
end

puts "Answer: %d" % largest_palindrome