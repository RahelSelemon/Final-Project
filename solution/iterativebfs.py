from dataclasses import field
from typing import List, Tuple
import random
from sys import argv


START_CHAR = "S"
GOAL_CHAR = "$"
MOUNTAIN_CHAR = "#"
BLANK_CHAR = "-"


def build_puzzle(puzzle_file) -> list[list[str]]:
    puzzle_file = open(f'puzzles/{puzzle_file}', 'r', encoding='utf8')

    gridworld: list[list[str]] = []

    for line in puzzle_file.readlines():
        row = [marker for marker in line if marker != '\n'] 
        gridworld.append(row)

    return gridworld
        
def solve_puzzle(gridworld: list[list[str]]):
    num_rows = len(gridworld)
    num_cols = len(gridworld[0])

    start = [(r, c) for r in range(num_rows) for c in range(num_cols) if gridworld[r][c] == START_CHAR]
    goal  = [(r, c) for r in range(num_rows) for c in range(num_cols) if gridworld[r][c] == GOAL_CHAR]

    return BFSsearch(start[0], goal[0], gridworld, num_rows, num_cols)

def isValidLoc(world, num_rows, num_cols, r_pos, c_pos):
    if r_pos >= 0 and r_pos < num_rows and c_pos >= 0 and c_pos < num_cols:
        if world[r_pos][c_pos] != MOUNTAIN_CHAR:
            return True
    return False

def getValidChildren(world, loc, num_rows, num_cols):
    children = []
    if isValidLoc(world, num_rows, num_cols, loc[0] - 1, loc[1]):
        children.append((loc[0] - 1, loc[1]))
    if isValidLoc(world, num_rows, num_cols, loc[0] + 1, loc[1]):
        children.append((loc[0] + 1, loc[1]))
    if isValidLoc(world, num_rows, num_cols, loc[0], loc[1] - 1):
        children.append((loc[0], loc[1] - 1))
    if isValidLoc(world, num_rows, num_cols, loc[0], loc[1] + 1):
        children.append((loc[0], loc[1] + 1))
    return children

def pathfinder(parents, start, goal):
    path = [goal]
    while path[-1] != start:
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

def showPuzzle(current_location, world):
    num_rows = len(world)
    num_cols = len(world[0])
    for row in range(num_rows):
        rowstr = ""
        for col in range(num_cols):
            if (row,col) == current_location: 
                rowstr += "*"
            else: 
                rowstr += world[row][col]
        print(rowstr)

def markPath(world, path):
    num_rows = len(world)
    num_cols = len(world[0])
    if len(path) > 2:
        for row in range(num_rows):
            rowstr = ''
            for col in range(num_cols):
                if (row,col) in path[1:len(path) - 1]: 
                    rowstr += "*"
                else: 
                    rowstr += world[row][col]
            print(rowstr)


if __name__ == '__main__':
    if(len(argv) != 2): 
        raise ValueError(f'Please enter a single puzzle filename (within the `puzzles` folder) as an argument.')
    puzzle = build_puzzle(argv[1])
    print("Maze layout:\n++++++++++++++++++")
    showPuzzle(None, puzzle)
    path = solve_puzzle(puzzle)
    print("\nSolution path:\n+++++++++++++++++")
    markPath(puzzle, path)
