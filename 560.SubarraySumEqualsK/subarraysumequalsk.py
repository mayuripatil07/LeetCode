class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        d = {0:1}
        s = 0
        for i in nums:
            s += i
            if s - k in d:
                count += d[s-k]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return count
