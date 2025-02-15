def twoSum(nums: list[int], target: int) -> list[int]:
    table = {}

    for index, num in enumerate(nums):
        if target - num in table:
            return [table[target - num], index]
        table[num] = index