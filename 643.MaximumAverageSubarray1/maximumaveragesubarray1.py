class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -math.inf
        window_start = 0
        s = 0
        count = 0
        for window_end in range(0,len(nums)):
            s += nums[window_end]
            count += 1
            if count == k:
                count -= 1
                avg = s / k
                max_avg = max(max_avg, avg)
                s -= nums[window_start]
                window_start += 1
        return max_avg
            
