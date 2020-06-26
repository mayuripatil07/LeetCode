class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        s = 0
        for n in nums:
            s += n
            result.append(s)
        return result
