### Jaime Alvarez - August 2016

=begin
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
=end

smallest = 0
i = 1
flag = false

while true do
  (1..20).each do |k|
    unless i % k == 0
      flag = false
      break
    end
    flag = true
  end
  
  if flag
    smallest = i
    break
  end
  
  i += 1
end

puts "Smallest: %d" % smallest