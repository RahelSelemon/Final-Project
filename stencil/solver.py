from sys import argv

def build_puzzle(puzzle_file: str): # TODO: indicate the return type for the puzzle data
    # TODO: This function should take a file string (e.g. "puzzleX.txt") and return the puzzle data
    pass


def solve_puzzle(): # TODO: indicate the return type and function argument(s) along with types
    # TODO: This function should take the puzzle data and return the solution/path
    pass


def getValidNeighbors(): # Indicate the return type and function argument(s) along with types
    # *** Suggested helper function ***
        # The idea is to find all valid next steps from a given puzzle location
    pass


def showSolution(): # TODO: indicate the return type and function argument(s) along with types
    # TODO: Display your solution to us in any way you choose!
    pass


if __name__ == '__main__':
    if(len(argv) != 2): 
        raise ValueError(f'Please enter a single puzzle filename (within the `puzzles` folder) as an argument.')
    puzzle = build_puzzle(argv[1])
    path = solve_puzzle(puzzle)
    showSolution() # TODO: finish this once you decide what your argument(s) will be
