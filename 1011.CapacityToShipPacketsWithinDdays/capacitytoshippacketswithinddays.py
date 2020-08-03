class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low < high):
            capacity = 0
            mid = (low + high) // 2
            num_days = 1
            for wt in weights:
                capacity += wt
                if capacity > mid:
                    num_days += 1
                    capacity = wt

            if num_days <= D:
                high = mid
            else:
                low = mid + 1
        return low
                
