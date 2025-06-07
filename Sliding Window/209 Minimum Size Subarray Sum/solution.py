def minSubArrayLen(target: int, nums: list[int]) -> int:
    min_length = float("inf")
    current_sum = 0

    start = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum >= target:
            min_length = min(end - start + 1, min_length)
            current_sum -= nums[start]
            start += 1

    return min_length if min_length != float("inf") else 0