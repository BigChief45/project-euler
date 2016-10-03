## Jaime Alvarez -- October 2016

=begin
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

=end

power = 5
power_nums = []

i = 2
while i <= 1000000 do
  i_power_sum = i.to_s.split('').map(&:to_i).inject(0) { |pow, i| pow + (i**power) }
  power_nums << i if i_power_sum == i
  i += 1
end

p power_nums
puts "Sum of all numbers that can be written as the sum of the 5th of their digits: #{power_nums.inject(:+)}"