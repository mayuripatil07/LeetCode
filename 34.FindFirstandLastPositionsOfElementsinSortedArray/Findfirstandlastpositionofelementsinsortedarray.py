class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        result = []
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high-low)// 2
            if nums[mid] == target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1

        if low < len(nums) and nums[low] == target:
            result.append(low)
        else:
            result.append(-1)


        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high-low)// 2
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        if  nums[high] == target:
            result.append(high)
        else:
            result.append(-1)
        return result
