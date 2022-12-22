# https://www.codewars.com/kata/58663693b359c4a6560001d6/

def maze_runner(maze, directions):
    # Find the starting position of the runner in the maze
    x, y = 0, 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                x, y = i, j
                break

    # Follow the directions given
    for i in range(len(directions)):
        if directions[i] == "N":
            # Check if the next move is valid (not a wall or outside the maze)
            if x == 0 or maze[x - 1][y] == 1:
                return "Dead"
            else:
                x = x - 1
        elif directions[i] == "S":
            # Check if the next move is valid (not a wall or outside the maze)
            if x == len(maze) - 1 or maze[x + 1][y] == 1:
                return "Dead"
            else:
                x = x + 1
        elif directions[i] == "E":
            # Check if the next move is valid (not a wall or outside the maze)
            if y == len(maze[x]) - 1 or maze[x][y + 1] == 1:
                return "Dead"
            else:
                y = y + 1
        elif directions[i] == "W":
            # Check if the next move is valid (not a wall or outside the maze)
            if y == 0 or maze[x][y - 1] == 1:
                return "Dead"
            else:
                y = y - 1

        # Check if the runner has reached the finish point
        if maze[x][y] == 3:
            return "Finish"

    # If all moves have been made and the runner has not reached the finish point, return "Lost"
    return "Lost"
