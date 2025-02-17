def maxAreaOfIsland(grid: list[list[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    max_area = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                max_area = max(dfs(row, col), max_area)
    return max_area