local solution = {}

function solution.maze_runner(maze, directions)
    -- return string
    local x, y = 0, 0
    
    -- Find the starting position of the runner in the maze
    for i = 1, #maze do
        for j = 1, #maze[i] do
            if maze[i][j] == 2 then
                x, y = i, j
                break
            end
        end
    end

    -- Follow the directions given
    for i = 1, #directions do
        if directions[i] == "N" then
            -- Check if the next move is valid (not a wall or outside the maze)
            if x == 1 or maze[x - 1][y] == 1 then
                return "Dead"
            else
                x = x - 1
            end
        elseif directions[i] == "S" then
            -- Check if the next move is valid (not a wall or outside the maze)
            if x == #maze or maze[x + 1][y] == 1 then
                return "Dead"
            else
                x = x + 1
            end
        elseif directions[i] == "E" then
            -- Check if the next move is valid (not a wall or outside the maze)
            if y == #maze[x] or maze[x][y + 1] == 1 then
                return "Dead"
            else
                y = y + 1
            end
        elseif directions[i] == "W" then
            -- Check if the next move is valid (not a wall or outside the maze)
            if y == 1 or maze[x][y - 1] == 1 then
                return "Dead"
            else
                y = y - 1
            end
        end

        -- Check if the runner has reached the finish point
        if maze[x][y] == 3 then
            return "Finish"
        end
    end

    -- If all moves have been made and the runner has not reached the finish point, return "Lost"
    return "Lost"
end

return solution
