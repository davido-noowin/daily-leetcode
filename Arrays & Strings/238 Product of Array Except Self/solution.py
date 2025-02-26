def productExceptSelf(nums: list[int]) -> list[int]:
    left = 1
    right = 1
    left_array = [1] * len(nums)
    right_array = [1] * len(nums)

    for i in range(len(nums)):
        j = -i - 1
        left_array[i] = left
        left *= nums[i]
        right_array[j] = right
        right *= nums[j]
        
    return [l * r for l, r in zip(left_array, right_array)]