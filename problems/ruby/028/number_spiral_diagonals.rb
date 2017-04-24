## Jaime Alvarez -- October 2016

=begin
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
=end

class Grid
  attr_reader :dimension

  def initialize(dimension)
    @dimension = dimension
    @center = (dimension / 2).floor

    @grid = Array.new(dimension) { Array.new(dimension) }

    populate_grid
  end

  def diagonals_sum
    main_diagonal = (0..@dimension-1).collect { |i| @grid[i][i] }.reduce(:+)
    other_diagonal = (0..@dimension-1).collect { |i| @grid[i][-i-1] }.reduce(:+)

    (main_diagonal + other_diagonal) - 1 # remove the duplicated middle number, which is 1
  end

  def print_grid
    @grid.each do |row|
      row.each do |col|
        print "#{col}\t"
      end
      puts
    end
  end

  private

    def populate_grid(i=@dimension**2, row_start=0, col_start=@dimension-1, row_limit=@dimension-1, col_limit=0)
      # Right to left
      col_start.downto(col_limit) do |col|
        @grid[row_start][col] = i
        i -= 1
      end

      # Top to bottom
      (row_start+1).upto(row_limit) do |row|
        @grid[row][col_limit] = i
        i -= 1
      end

      # Left to right
      (col_limit+1).upto(col_start) do |col|
        @grid[row_limit][col] = i
        i -= 1
      end

      # Bottom to top
      (row_limit-1).downto(row_start+1) do |row|
        @grid[row][col_start] = i
        i -= 1
      end

      if (row_start == row_limit) && (col_start == col_limit)
        return
      end

      populate_grid(i, row_start+1, col_start-1, row_limit-1, col_limit+1)
    end
end

d = 1001
grid = Grid.new(d)
puts "the sum of the numbers on the diagonals in a #{d} by #{d} spiral is: #{grid.diagonals_sum}"