class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        left = 1
        for i in nums:
            result.append(left)
            left = left * i

        right = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * right
            right = right * nums[i]
        return result

            
