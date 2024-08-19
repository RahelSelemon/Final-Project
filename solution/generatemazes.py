import random

def initialize_maze(rows, cols):
    return [['#' for _ in range(cols)] for _ in range(rows)]

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def get_neighbors(r, c, rows, cols):
    neighbors = []
    if r > 1: neighbors.append((r-2, c))
    if r < rows-2: neighbors.append((r+2, c))
    if c > 1: neighbors.append((r, c-2))
    if c < cols-2: neighbors.append((r, c+2))
    random.shuffle(neighbors)
    return neighbors

def dfs_to_carve_path(maze, r, c, rows, cols, goal_r, goal_c):
    maze[r][c] = '-'
    for nr, nc in get_neighbors(r, c, rows, cols):
        if maze[nr][nc] == '#' and (nr, nc) != (goal_r, goal_c):
            maze[(r+nr)//2][(c+nc)//2] = '-'  # Carve the wall between cells
            dfs_to_carve_path(maze, nr, nc, rows, cols, goal_r, goal_c)

def generate_maze(rows, cols):
    maze = initialize_maze(rows, cols)
    
    # Randomly select start and goal positions
    sr, sc = random.randint(0, rows-1), random.randint(0, cols-1)
    gr, gc = random.randint(0, rows-1), random.randint(0, cols-1)
    
    while (sr, sc) == (gr, gc):
        gr, gc = random.randint(0, rows-1), random.randint(0, cols-1)
    
    maze[sr][sc] = 'S'
    maze[gr][gc] = '$'
    
    # Start DFS from start position
    dfs_to_carve_path(maze, sr, sc, rows, cols, gr, gc)
    
    # Ensure the goal is connected if not already
    if maze[gr][gc] == '#':
        maze[gr][gc] = '-'
    
    return maze


# Example usage:
rows, cols = 25, 25  # Dimensions of the maze
maze = generate_maze(rows, cols)
print_maze(maze)

#puzzleName = "puzzleBIG"
#puzzle_file = open(f'../puzzles/{puzzleName}', 'w', encoding='utf8')
#puzzle_file.write(maze)
