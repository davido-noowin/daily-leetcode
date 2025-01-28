def findClosestNumber(nums) -> int:
        largest_value = nums[0]

        for num in nums:
            if abs(num) < abs(largest_value):
                largest_value = num

        if largest_value < 0 and abs(largest_value) in nums:
            return abs(largest_value)

        return largest_value