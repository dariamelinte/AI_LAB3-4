# Lab 2 and 3: Modeling a decision problem

## Authors: Melinte Daria & Giosu Stefana - E3

### Problem: We have a 3x3 matrix with 8 cells numbered 1 to 8 and one empty cell. Knowing that the initial position of the cells is random and that we can move a cell only in place of the empty cell and only if it is adjacent to it, find, if there is one, a sequence of moves such that all cells are placed in ascending order in the matrix. After a cell is moved it cannot be moved again until one of its neighbors has been moved. The position of the empty cell does not matter for final state validation.


### Steps to solve:

- Choose a representation of a state of the problem. The representation must be explicit enough to contain all the necessary information to continue finding a solution, but it must also be formal enough to be easy to process/store.
- Identify the special states (initial and final) and implement the initialization function (takes as parameters the problem instance, returns the initial state) and the boolean function that checks whether a state received as a parameter is final.
- Implement transitions as functions that take a state and transition parameters and return the state resulting from applying the transition. Validation of transitions is done in one or more boolean functions with the same parameters.
- Implement the IDDFS strategy.


<3