# SudokuSolver

This is a simple sudoku solver (with bactrack) used for my study on CSP solvers.

<!-- TOC -->

- [SudokuSolver](#sudokusolver)
  - [Code division](#code-division)
  - [SudokuGame](#sudokugame)
  - [\_reset\_grid](#_reset_grid)
  - [input\_rows](#input_rows)
  - [SudokuSolver](#sudokusolver-1)
    - [\_isPossible](#_ispossible)
    - [solve](#solve)

<!-- /TOC -->

## Code division

There are two classes in the [main.py](src/main.py) file:
- SudokuGame
- SudokuSolver

Which are used to manage the game, and solve the game created.

## SudokuGame

This class contains the base of the sudoku game, but is missing the player controls, and most of the "game" itself. In this class we have two functions that we are going to use:
- _reset_grid
- input_rows


## _reset_grid

This functions is used to reset the game. It is important to note that "reset" means having an empty board.

## input_rows

This functions will read row by row the sequence of numbers to add to the grid.
For this study, no validation was added, and error may occur if a line is updated with invalid inforamtion.

## SudokuSolver

This class is used to control and solve the sudoku game object. when you instantiate this object, two things are set up. First, the sudoku game is referenced internally (when you modify the game grid in sudoku Solver, you also change it in the object itself). Second, the flag "hasSolution" is set to false. This flag is used to return afer the first solution is found.

> The solver assumes the initial grid is not violating any constrains

### _isPossible

This method is used to validate if the constrains are met. In a more complex CSP solver, this method would have more constrains, and validates if the option to be put under that cell (variable, in domain) is correct.

### solve

This Method is the main part of the solver. Understanding this part is essential to know how this CSP works.

First, we check if the flag hasSolution is true. This means that we found one solution in the solver, and we can return.

> this is also a hint that we are using recursion

the code then, goes cell by cell (skipping the already filled cells) and try all the options, one by one, using a BFS algorythm. Line 40 shows that we are updating the value, and then going forward by calling the `solve` method again. After that, we check if we found a solution. If not, we backtrack and go to the next possible number. This assumes the game is not broken, and one of the numbers **always** will be possible.

