def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (right + left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[right]