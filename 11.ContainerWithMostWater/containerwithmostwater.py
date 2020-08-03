class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        i = 0
        j = len(height) - 1
        max_area = 0
        width = len(height) - 1
        while(i <= j):
            if height[i] < height[j]:
                area = height[i] * width
                max_area = max(max_area, area)
                width -= 1
                i += 1
            elif height[i] >= height[j]:
                area = height[j] * width
                max_area = max(max_area, area)
                width -= 1
                j -= 1
        return max_area
