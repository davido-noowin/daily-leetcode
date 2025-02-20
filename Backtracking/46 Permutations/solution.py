def permute(nums: list[int]) -> list[list[int]]:
    res = []
    permutations = []

    def dfs():
        if len(permutations) == len(nums):
            res.append(permutations.copy())

        for num in nums:
            if num not in permutations:
                permutations.append(num)
                dfs()
                permutations.pop()
            
    dfs()
    return res