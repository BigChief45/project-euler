### Jaime Alvarez -- August 2016

=begin
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
=end

puts "Sum of all multiples of 3 or 5 below 1000 = "
puts (1..1000).to_a.select { |element| element % 3 == 0 || element % 5 == 0 }.inject(:+)
