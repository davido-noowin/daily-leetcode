def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1