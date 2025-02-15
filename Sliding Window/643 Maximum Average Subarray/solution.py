def findMaxAverage(nums: list[int], k: int) -> float:
    max_average = float('-inf')

    start = 0
    average = 0
    for end in range(len(nums)):
        average += nums[end]
        if end - start + 1 == k:
            max_average = max(max_average, average / k)
            average -= nums[start]
            start += 1

    return max_average