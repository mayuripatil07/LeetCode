class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            max_money = max(max_money, dp[i])
        dp = [0] * len(nums)
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            max_money = max(max_money, dp[i])
        return max_money
