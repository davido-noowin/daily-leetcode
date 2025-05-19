from collections import deque

def orangesRotting(self, grid: list[list[int]]) -> int:
    EMPTY, FRESH, ROTTEN = 0, 1, 2
    ROWS = len(grid)
    COLS = len(grid[0])
    num_fresh = 0
    queue = deque()

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == ROTTEN:
                queue.append((i, j))
            elif grid[i][j] == FRESH:
                num_fresh += 1
        
    if num_fresh == 0:
        return 0

    time = -1
    while queue:
        time += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for r, c in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == FRESH:
                    grid[r][c] = ROTTEN
                    num_fresh -= 1
                    queue.append((r, c))

    return time if num_fresh == 0 else -1