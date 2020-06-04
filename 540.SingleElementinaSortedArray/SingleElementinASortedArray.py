class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count = 0
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high-low)//2
            if mid < len(nums)- 2 and nums[mid-1] < nums[mid] < nums[mid+1]:
                return nums[mid]
            if mid % 2 == 0:
                if mid < len(nums) - 2 and nums[mid] == nums[mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return nums[mid]
