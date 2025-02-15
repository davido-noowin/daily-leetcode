import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    nums = [-num for num in nums]
    heapq.heapify(nums)
    for i in range(k):
        res = heapq.heappop(nums)
    return -res