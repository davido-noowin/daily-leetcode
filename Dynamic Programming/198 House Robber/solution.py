def rob(nums: list[int]) -> int:
    dp = [0 for _ in range(len(nums))]

    if len(nums) == 1:
        return nums[0]

    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]