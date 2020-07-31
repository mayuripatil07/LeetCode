class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[high]:
                high -= 1
            elif nums[mid] > nums[high]:
                if nums[mid] > target and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
