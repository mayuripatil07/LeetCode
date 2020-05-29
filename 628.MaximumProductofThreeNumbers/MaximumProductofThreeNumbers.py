class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[-1] * nums[-2] * nums[-3]
        n = nums[0] * nums[1] * nums[-1]
        p = nums[0] * nums[1] * nums[2]
        result = max(m,n,p)
        return result
    
