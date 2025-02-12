def containsDuplicate(nums: list[int]) -> bool:
    duplicate = set(nums)

    return len(duplicate) != len(nums)