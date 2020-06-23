class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , j = 0, 0
        end = len(nums) - 1
        while(j <= end):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[end] = nums[end], nums[j]
                end -= 1
            else:
                j += 1
