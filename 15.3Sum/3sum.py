class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        i = 0
        for i in range(len(nums)-2):
            if i > 1 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while(left < right):
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    result.add((nums[i],nums[left],nums[right]))
                    left += 1
                    while (nums[left] == nums[left-1] and left < right):
                        left += 1
                elif target < 0:
                    left += 1
                    while (nums[left] == nums[left-1] and left < right):
                        left += 1
                elif target > 0:
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1




        return list(result)

                        
