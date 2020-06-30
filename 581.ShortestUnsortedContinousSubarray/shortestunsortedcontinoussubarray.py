class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        count = 0
        sorted_nums = sorted(nums)
        start, end = 0, -1
        i = 0
        while(i < len(nums)):
            if nums[i] != sorted_nums[i]:
                start =  i
                break
            i += 1

        i = len(nums) - 1
        while(i >= 0):
            if nums[i] != sorted_nums[i]:
                end = i
                break
            i -= 1

        return end - start + 1
    
