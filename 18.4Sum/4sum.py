class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                while(left < right):
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        while (left < right and nums[left] == nums[left-1]):
                            left += 1
                    elif sum_ < target:
                        left += 1
                        while (left < right and nums[left] == nums[left-1]):
                            left += 1
                    elif sum_ > target:
                        right -= 1
                        while(left < right and nums[right] == nums[right+1]):
                            right -= 1

        return list(result)

            
