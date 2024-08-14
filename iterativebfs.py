from dataclasses import field
from typing import List, Tuple

START_CHAR = "S"
GOAL_CHAR = "$"
MOUNTAIN_CHAR = "#"
BLANK_CHAR = "-"

# # Structure representing a Gridworld node
# class GridNode:
#     # Represents the (x, y) coordinates of the node
#     loc_pair: Tuple[int, int]
#     # All NSEW neighbors of the node (note there may not be neighbors in all 4 directions)
#     neighbors: List['GridNode'] = field(default_factory=list)

#     def add_neighbor(self, neighbor_node: 'GridNode'):
#         self.neighbors.append(neighbor_node)

def build_puzzle(puzzle_file) -> list[list[str]]:
    puzzle_file = open(f'puzzles/{puzzle_file}', 'r', encoding='utf8')
    # num_rows = int(puzzle_file.readline())
    # num_cols = int(puzzle_file.readline())
    world: list[list[str]] = []

    for line in puzzle_file.readlines():
        row = [marker for marker in line if marker != '\n'] 
        world.append(row)

    return world
        
def solve_puzzle(gridworld: list[list[str]]):
    num_rows = len(gridworld)
    num_columns = len(gridworld[0])

    start = [(r, c) for r in range(len(gridworld)) for c in range(len(gridworld[r])) if gridworld[r][c] == START_CHAR]
    goal  = [(r, c) for r in range(len(gridworld)) for c in range(len(gridworld[r])) if gridworld[r][c] == GOAL_CHAR]

    return BFSsearch(start[0], goal[0], gridworld, num_rows, num_columns)

def isValidLoc(world, num_row, num_col, rowPos, colPos):
    if rowPos >= 0 and rowPos < num_row and colPos >= 0 and colPos < num_col:
        if world[rowPos][colPos] != MOUNTAIN_CHAR:
            return True
    return False

def getValidChildren(world, loc, num_row, num_col):
    children = []
    if isValidLoc(world, num_row, num_col, loc[0] - 1, loc[1]):
        children.append((loc[0] - 1, loc[1]))
    if isValidLoc(world, num_row, num_col, loc[0] + 1, loc[1]):
        children.append((loc[0] + 1, loc[1]))
    if isValidLoc(world, num_row, num_col, loc[0], loc[1] - 1):
        children.append((loc[0], loc[1] - 1))
    if isValidLoc(world, num_row, num_col, loc[0], loc[1] + 1):
        children.append((loc[0], loc[1] + 1))
    return children

def pathfinder(parents, start, goal):
    path = [goal]
    while path[-1] != start:
        #print(path[-1])
        path.append(parents[path[-1]])
    path.reverse()
    return path

def BFSsearch(start, goal, world, num_row, num_col): 
    '''Search for the `goal`, starting from the `current_location`. Avoid already `visited` locations.'''
    # initialize todo list
    todo = [start]

    # initilize visited set
    visited = set(start)

    parents = {}

    while len(todo) != 0:
        # "pop" the next stop from this location from todo
        current = todo[0] 
        todo = todo[1:] 

        for loc in getValidChildren(world, current, num_row, num_col):
            if loc not in visited:
                parents[loc] = current
                if loc == goal:
                    return pathfinder(parents, start, goal)
                todo.append(loc)
                visited.add(loc)
            
    return None

def showPos(current_location, world, num_rows, num_columns):
    for row in range(num_rows):
        rowstr = ''
        for col in range(num_columns):
            if (row,col) == current_location: 
                rowstr += "*"
            else: 
                rowstr += world[row][col]
        print(rowstr)


def markPath(world, path):
    num_rows = len(world)
    num_cols = len(world[0])
    for row in range(num_rows):
        rowstr = ''
        for col in range(num_cols):
            if (row,col) in path: 
                rowstr += "*"
            else: 
                rowstr += world[row][col]
        print(rowstr)

if __name__ == '__main__':
    # The `argv` variable will give all arguments to the program received at the terminal.
    # The first argument is the name of the Python file, so we ignore it.
    from sys import argv
    if(len(argv) != 2): 
        raise ValueError(f'Please enter a single puzzle filename (within the `puzzles` folder) as an argument.')
    puzzle = build_puzzle(argv[1])
    path = solve_puzzle(puzzle)
    markPath(puzzle, path)
