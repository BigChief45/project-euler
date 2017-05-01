## Jaime Avarez - May 2017

=begin
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
=end

require 'prime'

def combinations?(a, b)
  a.to_s.split('').sort == b.to_s.split('').sort
end

# Get 4-digit primes
four_digit_primes = Prime.take_while { |p| p.to_s.size <= 4 }.select { |i| i.to_s.size == 4 }
sequences = []

four_digit_primes.each do |prime1|
  sequence = []
  sequence << prime1

  # Compare to other primes
  four_digit_primes.drop(four_digit_primes.index(prime1)).each do |prime2|
    next if prime1 == prime2
    sequence << prime2 if combinations?(prime1, prime2)
  end

  sequences << sequence if sequence.size == 3
end

# Now check that each prime in the sequence is separated by n
answer = []
sequences.each do |sequence|
  if sequence[2] - sequence[1] == sequence[1] - sequence[0]
    answer = sequence
    break
  end
end

p "The sequence is #{answer}"
puts "Concatenation of this sequence is #{answer.join}"