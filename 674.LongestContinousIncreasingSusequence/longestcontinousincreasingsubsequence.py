class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_res = 0
        count = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                count += 1
                max_res = max(max_res, count)
            else:
                count = 1
        return max_res
