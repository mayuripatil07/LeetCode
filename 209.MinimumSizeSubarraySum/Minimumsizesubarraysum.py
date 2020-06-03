class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = math.inf
        window_end = 0
        window_start = 0
        sum_ = 0
        for window_end in range(len(nums)):
            sum_ += nums[window_end]

            while(sum_ >= s):
                min_length = min(min_length, window_end - window_start + 1)
                sum_ -= nums[window_start]
                window_start += 1

        if min_length == math.inf:
            return 0
        else:
            return min_length
