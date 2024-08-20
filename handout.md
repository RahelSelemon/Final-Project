# Final Project: Escape From Gridworld

_Can you find a path from a start location to goal location in a gridworld maze?_

##### Getting started:

1. Create a [GitHub](https://github.com/) account if you don't already have one.
2. Clone [this](https://github.com/RahelSelemon/Final-Project-Mosaic24) GitHub repository into a directory of your choosing.
3. Explore - Open the "puzzles" folder. We have provided a few puzzle files for you to test your implementation with.
4. Open the stencil.py file. This is what you will be working in for most of the assignment.

We have already written a few important function headers for you but you will be responsible for filling in the function bodies and splitting up the work into helper functions. Your main reponsiblities are indicated with a "TODO" comment.

As you have now seen, each puzzle/maze is in the form of a Gridworld. A Gridworld is a representation of 2D space often used when programming. To identify the location of a particular cell we use a coordinate pair which is (row #, column #) instead of (x, y). Gridworld is different than other coordinate planes you've used before since the topmost-leftmost cell starts at (0, 0). From most cells in the Gridworld, you can move up/down/left/right at a single step. Given a grid location (r, c), it should be simple enough to find the locations of the cells directly above/below/either side, right? Cool!

Now think about how YOU might choose to represent a Gridworld in Python.

##### Puzzle Files

Our files represent each cell with different characters: "S" is the start, "\#" is the goal, "-" is a blank/free space, and "\$" is a mountain/barrier which you cannot occupy. It is important to note that we will only expect your solution to work for puzzles with exactly one "S" cell and one "$" cell.

By now you have noticed that the puzzles can come in all sorts of layouts and dimensions. Use your Python FileIO skills to read in the text file data and figure and store that data in any form that you find useful.

We also encourage you to make more of your own puzzle files to test on. They should be text files (.txt) located in the "puzzles" folder, designed in a similar format. Having more test cases never hurts!

## Our expectations:

- Collaborate with your neighbors, brainstorm ideas, make friends, but don't copy code
- Use online resources and refer to program materials but don't use a chatbot
- Do not change what is already part of the stencil without running it by one of the TAs first
- Ask for help as frequently as you need but we do encourage you to STRUGGLE a bit
