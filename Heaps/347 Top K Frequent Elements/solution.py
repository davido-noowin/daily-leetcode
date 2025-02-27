import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    nums_count = [(-val, key) for key, val in count.items()]
    heapq.heapify(nums_count)

    res = []
    for _ in range(k):
        frequency, output = heapq.heappop(nums_count)
        res.append(output)

    return res