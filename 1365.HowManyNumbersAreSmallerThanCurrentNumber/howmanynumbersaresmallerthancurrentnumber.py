class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        n = sorted(nums)
        for i in nums:
            a.append(n.index(i))
        return a
