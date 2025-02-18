def numIslands(grid: list[list[str]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    def dfs(i, j):
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == "0":
            return
        else:
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    num_islands = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                dfs(row, col)
                num_islands += 1
        
    return num_islands