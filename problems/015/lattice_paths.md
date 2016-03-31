# Problem #15 - Lattice Paths

![Lattice Grid Example](https://projecteuler.net/project/images/p015.gif)

> Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
> How many such routes are there through a 20x20 grid?


## SOLUTION

*Jaime Alvarez - March 2016*

This problem does not require programming. 

From this source: [http://www.robertdickau.com/manhattan.html](http://www.robertdickau.com/manhattan.html):

>... each of the points is described by the binomial coefficients, and the sequence of path counts for lattices of different sizes is 1, 2, 6, 20, 70, …, also known as the central binomial
>coefficients.

According to the source, the total amount of lattice pathways in a *n x n* grid is equal to twice *n* combination of *n*. In other words, the total amount of pathways is equal to the following (where *n* is the dimension of the grid):

![Combination Formula](http://www.robertdickau.com/cbc1.gif)

Since *n = 20* for a 20x20 grid, we can simply use a [combination calculator](http://www.calculatorsoup.com/calculators/discretemathematics/combinations.php) to obtain the answer: **137846528820**