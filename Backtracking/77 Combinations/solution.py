def combine(n: int, k: int) -> list[list[int]]:
    res = []
        
    combination = []
    def backtrack(position):
        if len(combination) == k:
            res.append(combination.copy())
            return
            
        for i in range(position, n + 1):
            combination.append(i)
            backtrack(i + 1)
            combination.pop()

    backtrack(1)
    return res