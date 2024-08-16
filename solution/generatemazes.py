def generate_maze(rows, cols):
    # Create an empty maze
    maze = [['-' for _ in range(cols)] for _ in range(rows)]

    # Place the start (S) and end ($) cells
    maze[0][0] = 'S'
    maze[rows-1][cols-1] = '$'

    # Add barriers (#) to the maze randomly but ensure there's a path
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == '-' and random.random() < 0.3:
                maze[r][c] = '#'

    # Make sure the path from 'S' to '$' is clear (simplified)
    for r in range(1, rows-1):
        maze[r][0] = '-'
    for c in range(1, cols-1):
        maze[rows-1][c] = '-'

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

# rows, cols = 6, 6  # change
# maze = generate_maze(rows, cols)
# print_maze(maze)