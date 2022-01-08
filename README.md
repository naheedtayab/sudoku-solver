# sudoku-solver
Sudoku solver using backtracking technique

This is a sudoku solver in python that can take any valid input sudoku with empty cells that need to be solved.

To do this, it uses backtracking technique by trying an input for each cell but as soon as it finds a cell with no valid 1-9 input, it will go back to the previous altered cell and try a new number for that.

Also, the solver shows how long it took to solve the puzzle which can be useful if you want to compare it to how fast a different approach might be. 
