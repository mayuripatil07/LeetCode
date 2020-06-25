class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target > nums[-1]:
                return len(nums)
        if target < nums[0]:
                return 0

        for i in range(0,len(nums)):
            if nums[i] == target:
                return i

        for i in range(1,len(nums)):
            if nums[i-1] < target < nums[i]:
                return i

            
