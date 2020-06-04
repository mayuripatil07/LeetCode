class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        flag = 0
        for n in range(1,len(nums)):
            if nums[n] > nums[n-1]:
                flag = 1
                continue
            else:
                flag = 0
                break

        while(low <= high):
            mid = low + (high-low)//2
            if nums[mid] < nums[0] and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] >= nums[0]:
                low = mid + 1
            else:
                high = mid - 1

        if flag == 1:
            return nums[0]
        else:
            return nums[mid]
