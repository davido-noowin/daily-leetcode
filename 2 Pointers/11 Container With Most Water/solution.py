def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        rectangle_height = min(height[left], height[right])
        area = rectangle_height * (right - left)
        max_water = max(area, max_water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
    return max_water