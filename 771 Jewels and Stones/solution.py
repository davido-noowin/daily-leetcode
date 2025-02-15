def numJewelsInStones(jewels: str, stones: str) -> int:
    jewel_counter = {}
    for jewel in jewels:
        jewel_counter[jewel] = 0

    for stone in stones:
        if stone in jewel_counter:
            jewel_counter[stone] += 1

    return sum(jewel_counter.values())