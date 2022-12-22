# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    if not snail_map:
        return []

    # Initialize variables to track the current position and direction of the snail
    row = 0
    col = 0
    direction = 0  # 0 = right, 1 = down, 2 = left, 3 = up

    # Initialize the result array
    result = []

    # Initialize the number of rows and columns in the snail_map
    num_rows = len(snail_map)
    num_cols = len(snail_map[0])

    # Initialize a visited matrix to track which elements have been visited
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    # Traverse the snail_map in a snailshell pattern until all elements have been visited
    while len(result) < num_rows * num_cols:
        # Add the current element to the result array
        result.append(snail_map[row][col])
        visited[row][col] = True

        # Move to the next element based on the current direction
        if direction == 0:  # right
            if col + 1 < num_cols and not visited[row][col + 1]:
                col += 1
            else:
                direction = 1
                row += 1
        elif direction == 1:  # down
            if row + 1 < num_rows and not visited[row + 1][col]:
                row += 1
            else:
                direction = 2
                col -= 1
        elif direction == 2:  # left
            if col - 1 >= 0 and not visited[row][col - 1]:
                col -= 1
            else:
                direction = 3
                row -= 1
        elif direction == 3:  # up
            if row - 1 >= 0 and not visited[row - 1][col]:
                row -= 1
            else:
                direction = 0
                col += 1

    return result