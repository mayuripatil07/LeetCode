class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = nums[0]
        val = 0
        for i in nums:
            val += i
            min_value = min(val, min_value)
        return max((1-min_value), 1)
